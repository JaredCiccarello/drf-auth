from rest_framework import generics
from .serializer import CameraSerializer
from .models import camera
from .permissions import IsOwnerOrReadOnly


class CameraList(generics.ListCreateAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    queryset = camera.objects.all()
    serializer_class = CameraSerializer


class CameraDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = camera.objects.all()
    serializer_class = CameraSerializer

# Create your views here.
