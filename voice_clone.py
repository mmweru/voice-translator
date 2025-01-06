# File: voice_clone.py
import torch
from tortoise.api import TextToSpeech
from tortoise.utils.audio import load_audio, load_voice, load_voices

class VoiceCloner:
    def __init__(self):
        self.tts = TextToSpeech()
        
    def clone_voice(self, reference_audio_path, text, output_path):
        # Load the reference audio
        reference_audio = load_audio(reference_audio_path, 22050)
        
        # Generate speech with cloned voice
        gen = self.tts.tts_with_preset(
            text,
            voice_samples=[reference_audio],
            preset='fast',
            k=1
        )
        
        torchaudio.save(output_path, gen.squeeze(0).cpu(), 22050)
        return output_path
