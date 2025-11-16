🚀 Speech Recognition Web App (Whisper Fine-Tuned + Django + TTS)

This is a full-stack speech transcription system powered by a fine-tuned Whisper model, deployed inside a Django backend with browser-based audio recording, file upload, and Text-to-Speech (TTS) output.

🎯 Fine-Tuned Whisper Model (900MB)

The fine-tuned Whisper model is too large to store on GitHub (~900MB).
Download it manually and place it inside the whisper-finetuned/ folder.

🔽 Download the model (Google Drive)

https://drive.google.com/uc?export=download&id=15GNsX30ibuSnIulfHJ2A2vXsnTiWLpHI

📂 After downloading/extracting, place files here:
whisper-finetuned/
    model.safetensors
    config.json
    preprocessor_config.json
    tokenizer_config.json
    generation_config.json
    merges.txt
    vocab.json
    special_tokens_map.json
    normalizer.json
    added_tokens.json


This folder must exist exactly like this for the app to run.

🧰 Tech Stack
Backend
Python 3.10
Django 5.2+
Fine-tuned Whisper model (safetensors)
PyTorch 2.9 (CPU)
ffmpeg for audio decoding
pyttsx3 for TTS
Frontend
HTML
CSS
Vanilla JavaScript
Browser-based microphone recording

📂 Project Structure
speech_project/
│
├── speech_app/
│   ├── templates/speech_app/
│   │   ├── index.html
│   │   ├── upload.html
│   │   └── record.html
│   ├── static/
│   │   ├── styles.css
│   │   └── js/main.js
│   └── views.py
│
├── whisper-finetuned/
│   ├── config.json
│   ├── vocab.json
│   ├── merges.txt
│   ├── tokenizer_config.json
│   ├── normalizer.json
│   ├── generation_config.json
│   ├── special_tokens_map.json
│   ├── added_tokens.json
│   └── ❗ model.safetensors  → **NOT in repo**
│
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore

📥 Download Fine-Tuned Whisper Model
The model must be manually downloaded.
Download ZIP (Google Drive):
https://drive.google.com/uc?export=download&id=15GNsX30ibuSnIulfHJ2A2vXsnTiWLpHI

After downloading:
Extract the ZIP
move everything into:
speech_project/whisper-finetuned/
Ensure model.safetensors exists inside the folder

⚙️ Installation Guide

1️⃣ Create Virtual Environment
py -3.10 -m venv venvspeech310
venvspeech310\Scripts\activate

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Install ffmpeg (Required)
Download Windows build: https://www.gyan.dev/ffmpeg/builds/
Extract → rename folder to:
    C:\ffmpeg
Add to PATH:
    C:\ffmpeg\bin
Verify:
    ffmpeg -version

▶️ Run the Server
python manage.py runserver
Open in browser: http://127.0.0.1:8000/

🎤 Usage

Upload Audio

Go to /upload_audio/
Upload .wav / .mp3
Whisper transcribes audio
TTS generates voice output
Download .mp3 result

Record Audio

Go to /record_audio/
Record using microphone
Whisper transcribes instantly
TTS speaks the text
File saved automatically

🔊 Backend Flow (Whisper + TTS)

Receive uploaded audio or recording
Convert audio → WAV/PCM using ffmpeg
Load fine-tuned Whisper model

Generate transcription
Convert text → audio using pyttsx3
Save and return TTS output URL
Delete temp audio files

🛑 Important Notes

Whisper runs on CPU → FP16 is disabled
Model must be downloaded manually
Do NOT push model.safetensors to GitHub
Do NOT push virtual environments

🧹 .gitignore Highlights

venvspeech310/
venv/
*.safetensors
*.wav
*.mp3
*.zip
staticfiles/
db.sqlite3

🧪 Future Improvements

Real-time streaming transcription
Deploy on Render / Railway
React frontend
Multilingual mode
Speaker diarization (multi-speaker support)


<img width="1591" height="830" alt="Screenshot 2025-07-11 135058" src="https://github.com/user-attachments/assets/8641d92b-9a4d-4515-b976-17696589e167" />

