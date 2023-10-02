from django.urls import path
from . import views

urlpatterns = [
    path('api/screen-recordings/',
         views.create_screen_recording,
         name='create_screen_recording'),
    path('api/screenrecordings/',
         views.get_screen_recordings,
         name='get_screen_recordings'),
    path('upload/', views.upload_file, name='upload_file'),
    # Add more URL patterns as needed for your application
]
