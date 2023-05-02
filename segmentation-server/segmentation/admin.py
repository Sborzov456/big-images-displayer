from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Segmentation)
class SegmentationAdmin(admin.ModelAdmin):
    list_display = ('image_id', 'type')
    

@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    list_display = ('x', 'y', 'width', 'height', 'segmentation', 'get_type', 'get_image_id')
    search_fields = ['segmentation__id']

    @admin.display(ordering='segmentation__type', description='Type')
    def get_type(self, obj):
        return obj.segmentation.type
    
    @admin.display(ordering='segmentation__image_id', description='Image ID')
    def get_image_id(self, obj):
        return obj.segmentation.image_id


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
        return obj.segmentation.image_id
