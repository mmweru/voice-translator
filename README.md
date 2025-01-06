# Voice Translator with Speaker Cloning

A powerful voice translation system that not only translates speech between multiple languages but also preserves the speaker's voice in the translated output. Built with Python, this application uses state-of-the-art models for speech recognition, translation, and voice cloning.

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Framework](https://img.shields.io/badge/framework-Streamlit-red)

## ✨ Features

- **Real-time Voice Recording**: High-quality audio capture with noise reduction
- **Multilingual Support**: Translation between multiple languages including:
  - English
  - Spanish
  - French
  - German
  - Chinese
  - Japanese
  - Korean
  - Russian
  - Italian
  - Portuguese
- **Voice Cloning**: Preserves the speaker's voice characteristics in the translated speech
- **Noise Reduction**: Advanced audio preprocessing for better recognition
- **User-friendly Interface**: Built with Streamlit for easy interaction
- **File Upload Support**: Accept WAV and MP3 audio files
- **Adjustable Recording Duration**: Flexible recording time from 1-30 seconds

## 🛠️ Technologies Used

- **Whisper**: For accurate speech recognition
- **deep-translator**: For reliable text translation
- **XTTS v2**: For high-quality voice cloning and speech synthesis
- **Streamlit**: For the web interface
- **sounddevice**: For high-quality audio recording
- **noisereduce**: For audio preprocessing
- **PyDub**: For audio file handling

## 📋 Requirements

- Python 3.8 or higher
- Minimum 8GB RAM
- Microphone (for recording)
- Operating System: Windows/Linux/MacOS
- Internet connection (for model downloads)

## 🚀 Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/voice-translator.git
cd voice-translator
```

2. Create and activate virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

3. Install required packages
```bash
pip install -r requirements.txt
```

## 📖 Usage

1. Start the application:
```bash
streamlit run app.py
```

2. Select languages:
   - Choose source language (language you're speaking in)
   - Choose target language (language you want to translate to)

3. Record or upload audio:
   - Click "Record Audio" button and speak
   - Or upload an audio file (WAV/MP3)

4. Click "Translate" to process:
   - View original transcription
   - View translated text
   - Listen to translated audio in your voice

## 📁 Project Structure

```
voice_translator/
├── requirements.txt
├── config.py             # Configuration settings
├── audio_processor.py    # Audio recording and processing
├── translator.py         # Text translation
├── voice_synthesizer.py  # Voice cloning and synthesis
├── app.py               # Main Streamlit application
├── models/              # Downloaded model files
├── audio/              # Audio file storage
└── temp/               # Temporary file storage
```

## 🔍 Troubleshooting

1. **Recording Issues**:
   - Ensure microphone is properly connected
   - Check microphone permissions
   - Try recording in a quiet environment

2. **Voice Cloning Quality**:
   - Record at least 3-5 seconds of clear speech
   - Minimize background noise
   - Speak clearly and at a moderate pace

3. **Memory Issues**:
   - Ensure at least 8GB RAM is available
   - Close other resource-intensive applications

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- OpenAI's Whisper for speech recognition
- Coqui TTS team for XTTS voice cloning technology
- Streamlit team for the amazing web framework

## 📧 Contact

Your Name - mwerumaryann@gmail.com

Project Link: [https://github.com/yourusername/voice-translator](https://github.com/mmweru/voice-translator)
