"""
Voice Input - Speech recognition
"""

import logging
from typing import Dict

logger = logging.getLogger(__name__)


class VoiceInput:
    """Voice input handler"""
    
    def __init__(self, config: Dict = None):
        self.config = config or {}
        logger.info("✅ VoiceInput initialized")
    
    def listen(self) -> str:
        """Listen for voice command"""
        try:
            import speech_recognition as sr
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                audio = recognizer.listen(source, timeout=5)
                text = recognizer.recognize_google(audio, language="tr-TR")
                logger.info(f"🎤 Heard: {text}")
                return text
        except Exception as e:
            logger.error(f"Voice input error: {e}")
            return ""
