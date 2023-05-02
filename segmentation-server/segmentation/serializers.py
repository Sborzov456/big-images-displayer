from rest_framework import serializers
from .models import Box, Segmentation, Correction



class BoxSerializer(serializers.ModelSerializer):

    class Meta:
        model = Box
        fields = ('x', 'y', 'width', 'height')
        write_only_fields = ('segmentation', )

class SegmentationSerializer(serializers.ModelSerializer):

    boxes = BoxSerializer(many=True)

    def create(self, validated_data):
        segmentation = Segmentation.objects.create(image_id=validated_data['image_id'], type=validated_data['type'])
        for box in validated_data['boxes']:
            print(box)
            Box.objects.create(**box, segmentation=segmentation)
        return segmentation

    class Meta:
        model = Segmentation
        fields = ['boxes', 'type', 'image_id']


class CorrectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Correction
        fields = '__all__'