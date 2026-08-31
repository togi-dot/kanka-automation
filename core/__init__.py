"""Core automation package"""
from .automation_engine import AutomationEngine
from .agent_pool import AgentPool, Agent
from .llm_manager import LLMManager
from .task_manager import TaskManager

__all__ = ['AutomationEngine', 'AgentPool', 'Agent', 'LLMManager', 'TaskManager']
