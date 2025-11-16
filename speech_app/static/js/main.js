// main.js for record.html

let recorder, audioChunks = [];
const transcriptBox = document.getElementById("transcript");
const speechPlayer = document.getElementById("speechPlayer");
const processing = document.getElementById("processing");
const status = document.getElementById("recording-status");
const startBtn = document.getElementById("startBtn");
const stopBtn = document.getElementById("stopBtn");
const backBtn = document.getElementById("backBtn");

if (startBtn && stopBtn) {
    startBtn.onclick = async () => {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        recorder = new MediaRecorder(stream);
        audioChunks = [];

        recorder.ondataavailable = e => audioChunks.push(e.data);
        recorder.onstop = async () => {
            status.textContent = "Recording stopped. Processing...";
            status.style.color = "#00C851";

            const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
            const formData = new FormData();
            formData.append("audio_file", audioBlob, "recording.wav");

            processing.style.display = "block";

            try {
                const response = await fetch("/record_audio/", {
                    method: "POST",
                    body: formData
                });
                const data = await response.json();
                processing.style.display = "none";

                if (data.transcript) {
                    transcriptBox.value = data.transcript;
                    speechPlayer.src = data.speech_url + "?v=" + Date.now(); // cache-busting
                    speechPlayer.style.display = "block";
                    status.textContent = "✅ Transcription complete.";
                } else {
                    throw new Error(data.error || "Unknown error");
                }
            } catch (error) {
                status.textContent = "❌ Error during transcription.";
                transcriptBox.value = "Error: " + error.message;
            }
        };

        recorder.start();
        status.textContent = "🔴 Recording...";
        status.style.color = "#ff4444";
        startBtn.disabled = true;
        stopBtn.disabled = false;
    };

    stopBtn.onclick = () => {
        recorder.stop();
        startBtn.disabled = false;
        stopBtn.disabled = true;
    };

    backBtn.onclick = () => {
        window.history.back();
    };
}
