# File: app.py
import streamlit as st
from audio_processor import AudioProcessor
from translator import TranslationService
from voice_synthesizer import VoiceSynthesizer
from config import SUPPORTED_LANGUAGES, TEMP_DIR
import os

def initialize_session_state():
    if 'audio_processor' not in st.session_state:
        st.session_state.audio_processor = AudioProcessor()
    if 'translator' not in st.session_state:
        st.session_state.translator = TranslationService()
    if 'synthesizer' not in st.session_state:
        st.session_state.synthesizer = VoiceSynthesizer()

def main():
    st.set_page_config(
        page_title="Enhanced Voice Translator",
        layout="wide"
    )
    
    initialize_session_state()
    
    st.title("Enhanced Voice Translation System")
    
    # Sidebar for language selection
    st.sidebar.header("Language Settings")
    source_lang = st.sidebar.selectbox(
        "Source Language",
        list(SUPPORTED_LANGUAGES.keys()),
        index=0  # Default to English
    )
    target_lang = st.sidebar.selectbox(
        "Target Language",
        list(SUPPORTED_LANGUAGES.keys()),
        index=1  # Default to second language
    )
    
    # Main interface
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Input")
        duration = st.slider(
            "Recording Duration (seconds)",
            min_value=1,
            max_value=30,
            value=5
        )
        
        if st.button(f"Record Audio ({duration} seconds)"):
            with st.spinner("Recording..."):
                audio_file = st.session_state.audio_processor.record_audio(duration)
                if audio_file:
                    st.session_state['audio_file'] = audio_file
                    st.audio(audio_file)
                else:
                    st.error("Recording failed. Please check your microphone.")
        
        uploaded_file = st.file_uploader(
            "Or upload an audio file",
            type=['wav', 'mp3']
        )
        if uploaded_file:
            temp_path = os.path.join(TEMP_DIR, "uploaded.wav")
            with open(temp_path, "wb") as f:
                f.write(uploaded_file.getvalue())
            st.session_state['audio_file'] = temp_path
            st.audio(uploaded_file)
    

    with col2:
        st.header("Translation")
        if st.button("Translate") and 'audio_file' in st.session_state:
            with st.spinner("Processing..."):
                # Transcribe
                transcription = st.session_state.audio_processor.transcribe_audio(
                    st.session_state['audio_file'],
                    source_lang
                )
                if transcription:
                    st.text("Original Text:")
                    st.write(transcription)
                    
                    # Translate
                    translated_text = st.session_state.translator.translate(
                        transcription,
                        source_lang,
                        target_lang
                    )
                    st.text("Translated Text:")
                    st.write(translated_text)
                    
                    # Synthesize using the original audio as reference
                    output_path = os.path.join(TEMP_DIR, "translated.wav")
                    synthesized_audio = st.session_state.synthesizer.synthesize(
                        translated_text,
                        target_lang,
                        output_path,
                        st.session_state['audio_file']  # Pass the reference audio
                    )
                    
                    if synthesized_audio:
                        st.text("Translated Audio (in your voice):")
                        st.audio(synthesized_audio)
                    else:
                        st.error("Speech synthesis failed. Please try recording again.")
                else:
                    st.error("Transcription failed. Please try again.")

if __name__ == "__main__":
    main()