from django.shortcuts import render
from rest_framework.views import APIView
from .models import Segmentation, Correction, Image
from rest_framework.response import Response
from rest_framework import status
from .serializers import SegmentationSerializer, CorrectionSerializer, ImageUploadSerializer
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser

from .utils import get_segments

class ImageAPIView(generics.ListCreateAPIView):
    serializer_class = ImageUploadSerializer
    parser_classes = (MultiPartParser, FormParser)
    queryset = Image.objects.all()

    def post(self, request):

        response_data = super().create(request=request).data
        response_data['segmentations'] = []

        AI_data = get_segments(response_data['id'])
        print(AI_data)
        for segmentation in AI_data:
            segmentation_serializer = SegmentationSerializer(data=segmentation)
            segmentation_serializer.is_valid(raise_exception=True)
            segmentation_serializer.save()
            response_data['segmentations'].append(segmentation_serializer.data)
        return Response(response_data)


class SegmentationAPIView(APIView):
    def get(self, request):
        image_id = request.query_params['image_id']
        type = request.query_params['type']
        if type == 'all':
            segmentations = Segmentation.objects.all().filter(image_id=image_id)
            serializer = SegmentationSerializer(segmentations, many=True)
        else:
            segmentations = Segmentation.objects.all().filter(image_id=image_id, type=type)
            serializer = SegmentationSerializer(segmentations, many=True)
        return Response({'segmentations' : serializer.data})
     

    def post(self, request):
        data = request.data
        image_id = data['image']
        data = data['segmentations']
        for segmentation in data:
            segmentation['image'] = image_id
            serializer = SegmentationSerializer(data=segmentation)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        
        return Response(status=status.HTTP_201_CREATED)


class CorrectionAPIView(generics.ListCreateAPIView):
    serializer_class = CorrectionSerializer

    def get_queryset(self):
        queryset = Correction.objects.all().filter(segmentation__image_id=self.request.query_params.get('image_id'))
        return queryset
