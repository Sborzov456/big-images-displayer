from django.contrib import admin
from django.urls import path
from segmentation.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/cytology/segmentation', SegmentationAPIView.as_view())
]
