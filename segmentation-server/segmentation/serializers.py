from rest_framework import serializers
from .models import Polygon, Segmentation, Correction, Point

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
        segmentation = Segmentation.objects.create(image_id=validated_data['image_id'], type=validated_data['type'])
        for polygon in validated_data['polygons']:
            new_polygon = Polygon.objects.create(segmentation=segmentation)
            for point in polygon['points']:
                Point.objects.create(**point, polygon=new_polygon)
        return segmentation

    class Meta:
        model = Segmentation
        fields = ['polygons', 'type', 'image_id']


class CorrectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Correction
        fields = '__all__'