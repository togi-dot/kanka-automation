"""
Task Manager - Handles task creation, execution, and tracking
"""

import logging
import uuid
from typing import Dict, Any, List
from datetime import datetime

logger = logging.getLogger(__name__)


class TaskManager:
    """Manages task lifecycle"""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.tasks: Dict[str, Dict] = {}
        self.running = False
        logger.info("✅ TaskManager initialized")
    
    def create_task(self, description: str, plan: Dict, agent_id: str) -> str:
        """Create new task"""
        task_id = str(uuid.uuid4())[:8]
        self.tasks[task_id] = {
            "id": task_id,
            "description": description,
            "plan": plan,
            "agent_id": agent_id,
            "status": "pending",
            "created_at": datetime.now(),
            "completed_at": None
        }
        logger.info(f"📋 Task created: {task_id}")
        return task_id
    
    def start(self):
        """Start task manager"""
        self.running = True
        logger.info("▶️  TaskManager started")
    
    def stop(self):
        """Stop task manager"""
        self.running = False
        logger.info("⏹️  TaskManager stopped")
