# File: audio_processor.py
import sounddevice as sd
import scipy.io.wavfile
import whisper
import numpy as np
from pydub import AudioSegment
import noisereduce as nr
from config import SUPPORTED_LANGUAGES, SAMPLE_RATE, CHANNELS, TEMP_DIR
import wave
import os

class AudioProcessor:
    def __init__(self):
        self.whisper_model = whisper.load_model("medium")  # Using medium model for better accuracy
        
    def record_audio(self, duration):
        try:
            print("Recording...")
            # Record audio with higher quality
            recording = sd.rec(
                int(duration * SAMPLE_RATE),
                samplerate=SAMPLE_RATE,
                channels=CHANNELS,
                dtype='float32'
            )
            sd.wait()
            print("Recording finished.")
            
            # Normalize audio
            recording = np.clip(recording, -1, 1)
            
            # Apply noise reduction
            reduced_noise = nr.reduce_noise(
                y=recording.flatten(),
                sr=SAMPLE_RATE,
                prop_decrease=0.95,
                n_std_thresh_stationary=1.5
            )
            
            # Save processed audio
            temp_path = os.path.join(TEMP_DIR, "recorded.wav")
            scipy.io.wavfile.write(temp_path, SAMPLE_RATE, reduced_noise)
            
            return temp_path
            
        except Exception as e:
            print(f"Recording error: {e}")
            return None
    
    def transcribe_audio(self, audio_path, source_lang="en"):
        try:
            # Load and preprocess audio
            audio = AudioSegment.from_file(audio_path)
            
            # Convert to mono if stereo
            if audio.channels > 1:
                audio = audio.set_channels(1)
            
            # Normalize audio
            audio = audio.normalize()
            
            # Export processed audio
            temp_path = os.path.join(TEMP_DIR, "processed.wav")
            audio.export(temp_path, format="wav")
            
            # Transcribe with language hint
            lang_code = SUPPORTED_LANGUAGES.get(source_lang, "en")
            result = self.whisper_model.transcribe(
                temp_path,
                language=lang_code,
                fp16=False,  # Disable half-precision for better accuracy
                condition_on_previous_text=True,
                initial_prompt="This is a clear voice recording."
            )
            
            return result['text']
            
        except Exception as e:
            print(f"Transcription error: {e}")
            return ""
