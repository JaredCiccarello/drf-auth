from rest_framework import serializers
from .models import camera


class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'velocity', 'seen_by', 'description', 'updated_at', 'created_at')
        model = camera