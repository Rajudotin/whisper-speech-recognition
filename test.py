import os
import whisper

# ✅ Add ffmpeg to system PATH at runtime
os.environ["PATH"] += os.pathsep + r"C:\Quick Share\website\ffmpeg-7.1.1-full_build\bin"

model = whisper.load_model("base")
result = model.transcribe(r"C:\Quick Share\website\speech_project\common_voice_en_41910502.wav")
print("Transcript:", result["text"])
