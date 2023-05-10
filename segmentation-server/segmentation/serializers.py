from rest_framework import serializers
from .models import Polygon, Segmentation, Correction, Point, Image

class ImageUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('image_file', 'image_file_name', 'id')

class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = ['x', 'y']
        write_only_fields = ['polygon']

class PolygonSerializer(serializers.ModelSerializer):

    points = PointSerializer(many=True)

    class Meta:
        model = Polygon
        fields = ['points']
        write_only_fields = ['segmentation']

class SegmentationSerializer(serializers.ModelSerializer):

    polygons = PolygonSerializer(many=True)

    def create(self, validated_data):
        segmentation = Segmentation.objects.create(image=validated_data['image'], type=validated_data['type'])
        for polygon in validated_data['polygons']:
            new_polygon = Polygon.objects.create(segmentation=segmentation)
            for point in polygon['points']:
                Point.objects.create(**point, polygon=new_polygon)
        return segmentation

    class Meta:
        model = Segmentation
        fields = ['polygons', 'type', 'image']


class CorrectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Correction
        fields = '__all__'