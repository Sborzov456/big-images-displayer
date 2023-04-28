from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Segmentation)
class SegmentationAdmin(admin.ModelAdmin):
    list_display = ('patient_id', 'type')
    

@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    list_display = ('x', 'y', 'width', 'height', 'segmentation', 'get_type')
    search_fields = ['segmentation__patient_id']


    @admin.display(ordering='segmentation__type', description='Type')
    def get_type(self, obj):
        return obj.segmentation.type

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


# admin.site.register(Segmentation)

# admin.site.register(Box)
# # admin.site.register(Type)