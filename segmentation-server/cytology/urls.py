from django.contrib import admin
from django.urls import path
from segmentation.views import SegmentationAPIView, CorrectionAPIView, ImageAPIView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/cytology/segmentation/', SegmentationAPIView.as_view()),
    path('api/v1/cytology/correction/', CorrectionAPIView.as_view()),
    path('api/v1/cytology/upload', ImageAPIView.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
