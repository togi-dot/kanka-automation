"""
LLM Manager - Handles all LLM interactions
"""

import logging
import requests
from typing import Dict, Any, List
import json

logger = logging.getLogger(__name__)


class LLMManager:
    """Manages LLM interactions via Ollama"""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.host = self.config.get("ollama_host", "http://localhost:11434")
        self.model = self.config.get("model", "mistral")
        self.temperature = self.config.get("temperature", 0.7)
        self.max_tokens = self.config.get("max_tokens", 2048)
        
        logger.info(f"✅ LLMManager initialized with model: {self.model}")
    
    def generate_response(self, prompt: str) -> str:
        """Generate response from LLM"""
        try:
            response = requests.post(
                f"{self.host}/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "temperature": self.temperature,
                    "stream": False
                },
                timeout=30
            )
            
            if response.status_code == 200:
                return response.json().get("response", "")
            else:
                logger.error(f"LLM Error: {response.status_code}")
                return ""
        except Exception as e:
            logger.error(f"LLM connection error: {e}")
            return ""
    
    def generate_plan(self, task: str) -> Dict[str, Any]:
        """Generate execution plan for task"""
        prompt = f"""Analyze this task and create a step-by-step plan:
        Task: {task}
        
        Provide response as JSON with 'steps' array."""
        
        response = self.generate_response(prompt)
        try:
            return json.loads(response)
        except:
            return {"steps": [task]}
    
    def execute_step(self, step: str) -> Dict[str, Any]:
        """Execute a single step"""
        prompt = f"Execute: {step}"
        response = self.generate_response(prompt)
        return {"step": step, "result": response, "error": None}
