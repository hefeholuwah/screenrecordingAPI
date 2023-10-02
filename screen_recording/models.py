from django.db import models

class ScreenRecording(models.Model):
    # Define your fields here
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='screen_recordings/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class UploadedFile(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
