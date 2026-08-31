"""
Voice Output - Text to speech
"""

import logging
from typing import Dict

logger = logging.getLogger(__name__)


class VoiceOutput:
    """Voice output handler"""
    
    def __init__(self, config: Dict = None):
        self.config = config or {}
        logger.info("✅ VoiceOutput initialized")
    
    def speak(self, text: str):
        """Speak text"""
        try:
            import pyttsx3
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
            logger.info(f"🔊 Speaking: {text}")
        except Exception as e:
            logger.error(f"Voice output error: {e}")
