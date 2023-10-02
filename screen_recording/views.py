from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.files.base import ContentFile
from .models import ScreenRecording
from .serializers import ScreenRecordingSerializer  # You'll need to create this serializer

from django.shortcuts import render, redirect
from .forms import UploadFileForm

@api_view(['POST'])
def create_screen_recording(request):
    # Get the blob data from the request.FILES
    audio_blob = request.FILES.get('audio_blob')

    # Create a new ScreenRecording object with the blob data
    recording = ScreenRecording(title="Your Title", video_file=audio_blob)

    try:
        recording.save()
        return Response({"message": "Recording saved successfully"},
                        status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_screen_recordings(request):
    recordings = ScreenRecording.objects.all()
    serializer = ScreenRecordingSerializer(recordings, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_success')  # Redirect to a success page or another view
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})