from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import os
import uuid
import pyttsx3
import tempfile
import whisper
import os

# Add this early in views.py, before calling whisper
os.environ["PATH"] += os.pathsep + r"C:\QuickShare\website\ffmpeg-7.1.1-full_build\bin"

# Initialize model
MODEL = whisper.load_model("small", device="cpu")

# Base paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STATIC_DIR = os.path.join(BASE_DIR, "speech_project","speech_app", "static")

# Ensure FFmpeg is available
ffmpeg_path = R"C:\Quick Share\website\ffmpeg-7.1.1-full_build\bin"
if ffmpeg_path not in os.environ["PATH"]:
    os.environ["PATH"] += os.pathsep + ffmpeg_path

# 🏠 Home Page
def index(request):
    return render(request, "speech_app/index.html")

# 📤 Upload Audio Page
@require_http_methods(["GET", "POST"])
def upload_audio(request):
    if request.method == "POST" and request.FILES.get("audio_file"):
        return process_audio_request(request)
    return render(request, "speech_app/upload.html")

# 🎙️ Record Audio Page
@require_http_methods(["GET", "POST"])
def record_audio(request):
    if request.method == "POST" and request.FILES.get("audio_file"):
        return process_audio_request(request)
    return render(request, "speech_app/record.html", {"recording": True})

# 🔁 Transcribe Endpoint (used by record.js)
@require_http_methods(["POST"])
def transcribe_audio(request):
    if request.FILES.get("audio_file"):
        return process_audio_request(request)
    return JsonResponse({"error": "Invalid request"}, status=400)

# ♻️ Shared Logic for Upload/Record
def process_audio_request(request):
    try:
        print("[DEBUG] Received request")
        if "audio_file" not in request.FILES:
            return JsonResponse({"error": "No audio_file in request"}, status=400)

        audio_file = request.FILES["audio_file"]
        print(f"[DEBUG] Audio file name: {audio_file.name}")

        temp_path = os.path.join(tempfile.gettempdir(), str(uuid.uuid4()) + ".wav")
        with open(temp_path, "wb") as f:
            for chunk in audio_file.chunks():
                f.write(chunk)

        print(f"[DEBUG] Saved audio to: {temp_path}")

        result = MODEL.transcribe(temp_path)
        transcript = result.get("text", "")
        print(f"[DEBUG] Transcript: {transcript}")

        speech_url = generate_tts(transcript)
        print(f"[DEBUG] TTS generated at: {speech_url}")

        return JsonResponse({
            "transcript": transcript,
            "speech_url": speech_url
        })

    except Exception as e:
        print(f"[ERROR in process_audio_request]: {e}")
        return JsonResponse({"error": str(e)}, status=500)

# 🔊 Convert Transcript to Speech (TTS)
import time

import uuid

def generate_tts(transcript):
    if not transcript.strip():
        transcript = "No speech detected."

    # Generate unique filename
    filename = f"speech_{uuid.uuid4().hex}.mp3"
    tts_path = os.path.join(STATIC_DIR, filename)

    engine = pyttsx3.init()
    engine.setProperty('rate', 160)
    engine.setProperty('volume', 1.0)
    engine.save_to_file(transcript, tts_path)
    engine.runAndWait()

    if os.path.exists(tts_path):
        print(f"[SUCCESS] TTS created at {tts_path}")
        return f"/static/{filename}"
    else:
        print("[ERROR] File not written")
        return ""


# This file contains the main views for the speech recognition app.
# It handles the home page, audio upload, audio recording, and transcription.