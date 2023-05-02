from django.shortcuts import render
from rest_framework.views import APIView
from .models import Segmentation, Correction, Box
from rest_framework.response import Response
from rest_framework import status
from .serializers import SegmentationSerializer, CorrectionSerializer
from rest_framework import generics


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
        image_id = data['image_id']
        data = data['segmentations']
        for segmentation in enumerate(data):
            segmentation['image_id'] = image_id
            print(segmentation)
            serializer = SegmentationSerializer(data=segmentation)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        
        return Response(status=status.HTTP_201_CREATED)


class CorrectionAPIView(generics.ListCreateAPIView):
    serializer_class = CorrectionSerializer

    def get_queryset(self):
        queryset = Correction.objects.all().filter(segmentation__image_id=self.request.query_params.get('image_id'))
        return queryset
