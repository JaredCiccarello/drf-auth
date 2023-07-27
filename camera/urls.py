from django.urls import path
from .views import CameraList, CameraDetail

urlpatterns = [
    path('', CameraList.as_view(), name='camera_list'),
    path('<int:pk>', CameraDetail.as_view(), name='camera-detail'),
]