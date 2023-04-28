from django.shortcuts import render
from rest_framework.views import APIView
from .models import Box, Segmentation
# Create your views here.


class SegmentationAPIView(APIView):
    def get(self, request):
        patient_id = request.query_params['patient_id']
        boxes = Box.objects.all().filter(patient_id)
        return {'segmentation' : boxes}

    def post(self, request):
        print(request.data)
        data = request.data['1']
        print(data)
        Segmentation.objects.create(patiant_id=1, )