from django.contrib import admin
from django.urls import path
from segmentation.views import SegmentationAPIView, CorrectionAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/cytology/segmentation/', SegmentationAPIView.as_view()),
    path('api/v1/cytology/correction/', CorrectionAPIView.as_view())
]
