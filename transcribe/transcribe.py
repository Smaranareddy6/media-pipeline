import whisper
import torch
import numpy as np
import soundfile as sf
from whisper.audio import log_mel_spectrogram, pad_or_trim

def transcribe_audio(file_path):
    model = whisper.load_model("base")

    # Load audio directly with soundfile (bypasses ffmpeg completely)
    audio_data, sr = sf.read(file_path)
    if len(audio_data.shape) > 1:
        audio_data = np.mean(audio_data, axis=1)  # Convert stereo to mono

    # Resample if needed
    if sr != 16000:
        import librosa
        audio_data = librosa.resample(audio_data, orig_sr=sr, target_sr=16000)

    audio_tensor = torch.from_numpy(audio_data).float()
    audio_tensor = pad_or_trim(audio_tensor)

    mel = log_mel_spectrogram(audio_tensor).to(model.device)

    options = whisper.DecodingOptions(fp16=torch.cuda.is_available())
    result = whisper.decode(model, mel, options)

    return {"transcription": result.text}
