# File: translator.py
from deep_translator import GoogleTranslator
from config import SUPPORTED_LANGUAGES

class TranslationService:
    def translate(self, text, source_lang, target_lang):
        try:
            source_code = SUPPORTED_LANGUAGES.get(source_lang, "auto")
            target_code = SUPPORTED_LANGUAGES.get(target_lang, "en")
            
            translator = GoogleTranslator(
                source=source_code,
                target=target_code
            )
            
            result = translator.translate(text)
            return result
            
        except Exception as e:
            print(f"Translation error: {e}")
            return text
