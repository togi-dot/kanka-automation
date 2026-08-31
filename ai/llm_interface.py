"""
LLM Interface
"""

import logging

logger = logging.getLogger(__name__)


class LLMInterface:
    """Interface for LLM operations"""
    
    def __init__(self, llm_manager):
        self.llm = llm_manager
    
    def process_command(self, command: str) -> str:
        """Process natural language command"""
        return self.llm.generate_response(command)
