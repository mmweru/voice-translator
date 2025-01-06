# File: config.py
import os

# Directory structure
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(BASE_DIR, "models")
AUDIO_DIR = os.path.join(BASE_DIR, "audio")
TEMP_DIR = os.path.join(BASE_DIR, "temp")

# Create directories if they don't exist
for dir_path in [MODELS_DIR, AUDIO_DIR, TEMP_DIR]:
    os.makedirs(dir_path, exist_ok=True)

# Audio settings
SAMPLE_RATE = 44100  # Higher sample rate for better quality
CHANNELS = 1
CHUNK_SIZE = 2048

# Language configurations
SUPPORTED_LANGUAGES = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese": "zh",
    "Japanese": "ja",
    "Korean": "ko",
    "Russian": "ru",
    "Italian": "it",
    "Portuguese": "pt"
}
