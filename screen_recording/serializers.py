from rest_framework import serializers
from .models import ScreenRecording

class ScreenRecordingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScreenRecording
        fields = ('title', 'video_file')
