from django.urls import path
from .views import index, upload_audio, record_audio, transcribe_audio
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('upload_audio/', upload_audio, name='upload_audio'),
    path('record_audio/', record_audio, name='record_audio'),
    path('transcribe_audio/', transcribe_audio, name='transcribe_audio'),
  # adjust app name if different
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# This file defines the URL patterns for the speech_app application.
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('speech_app.urls')),  # adjust app name if different
# ]
#     "audio_file": audio_file.name,
# These URL patterns connect the speech recognition views:
# - '' → index: Home page
# - 'upload_audio/' → upload_audio: Upload page (GET/POST)
# - 'record_audio/' → record_audio: Recording page (GET/POST)
# - 'transcribe_audio/' → transcribe_audio: API endpoint for transcription
