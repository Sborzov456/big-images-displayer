from django.shortcuts import render
from rest_framework.views import APIView
from .models import Box, Segmentation
from rest_framework.response import Response
# Create your views here.
from rest_framework import status
from .utils import create_annotation
from .serializers import SegmentationSerializer



class AnnotationAPIView(APIView):
    def get(self, request):
        image_id = request.query_params['image_id']
        type = request.query_params['type']
        if type == 'all':
            segmentations = Segmentation.objects.all().filter(image_id=image_id)
        else:
            segmentations = Segmentation.objects.all().filter(image_id=image_id, type=type)
        boxes = Box.objects.all().filter(segmentation=segmentations).values()
        annotations = []
        for box in boxes:
            annotations.append(create_annotation(box['x'], box['y'], box['width'], box['height'], box['id']))
        return Response(annotations)

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