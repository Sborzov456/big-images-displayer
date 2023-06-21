from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_file_name')

@admin.register(Segmentation)
class SegmentationAdmin(admin.ModelAdmin):
    list_display = ('type', )
    
@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    list_display = ('x', 'y')


@admin.register(Polygon)
class PolygonAdmin(admin.ModelAdmin):
    list_display = ('id', 'segmentation', 'get_type', 'get_image_id')
    search_fields = ['segmentation__id']

    @admin.display(ordering='segmentation__type', description='Type')
    def get_type(self, obj):
        return obj.segmentation.type
    
    @admin.display(ordering='segmentation__image', description='Image ID')
    def get_image_id(self, obj):
        return obj.segmentation.image


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Correction)
class CorrectionAdmin(admin.ModelAdmin):
    list_display = ('correction', 'get_type', 'get_image_id')
    
    @admin.display(ordering='segmentation__type', description='Type')
    def get_type(self, obj):
        return obj.segmentation.type
    
    @admin.display(ordering='segmentation__image_id', description='Image ID')
    def get_image_id(self, obj):
        return obj.segmentation.image__id
