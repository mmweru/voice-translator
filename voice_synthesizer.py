# File: voice_synthesizer.py
from TTS.api import TTS
from config import SUPPORTED_LANGUAGES, TEMP_DIR
import os

class VoiceSynthesizer:
    def __init__(self):
        # Initialize XTTS with specific model for voice cloning
        self.tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2", progress_bar=True)
        
    def synthesize(self, text, lang_code, output_path, reference_audio_path):
        try:
            # Convert language code
            lang_code = SUPPORTED_LANGUAGES.get(lang_code, "en")
            
            # Generate speech with voice cloning from reference audio
            self.tts.tts_to_file(
                text=text,
                file_path=output_path,
                speaker_wav=reference_audio_path,  # Use the original recording as reference
                language=lang_code,
                speed=1.0
            )
            return output_path
            
        except Exception as e:
            print(f"Speech synthesis error: {e}")
            return None