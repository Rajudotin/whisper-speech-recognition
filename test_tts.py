import pyttsx3
import os

tts_path = "speech.mp3"
engine = pyttsx3.init()
engine.setProperty('rate', 160)
engine.setProperty('volume', 1.0)
engine.save_to_file("Hello! This is a test speech.", tts_path)
engine.runAndWait()

print(f"Done. File generated: {os.path.exists(tts_path)}")
# Check if the file was created successfully