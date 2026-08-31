"""
Agent Pool Management System
Handles dynamic agent creation, management, and scaling
"""

import logging
from typing import List, Optional, Dict, Any
import uuid
from datetime import datetime

logger = logging.getLogger(__name__)


class Agent:
    """Base agent class"""
    
    def __init__(self, agent_type: str = "generic"):
        self.id = str(uuid.uuid4())[:8]
        self.type = agent_type
        self.status = "idle"
        self.created_at = datetime.now()
        self.tasks_completed = 0
        self.last_active = datetime.now()
    
    def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Execute task"""
        self.status = "executing"
        self.last_active = datetime.now()
        
        try:
            result = {"status": "success", "agent_id": self.id}
            self.tasks_completed += 1
            self.status = "idle"
            return result
        except Exception as e:
            self.status = "error"
            return {"status": "failed", "error": str(e)}


class AgentPool:
    """Agent pool management"""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.agents: List[Agent] = []
        self.max_agents = self.config.get("max_agents", 5)
        self.auto_scale = self.config.get("auto_scale", True)
        
        # Initialize default agents
        self._init_default_agents()
        logger.info(f"✅ AgentPool initialized with {len(self.agents)} agents")
    
    def _init_default_agents(self):
        """Initialize default agents"""
        for i in range(min(3, self.max_agents)):
            agent = Agent(f"agent_{i}")
            self.agents.append(agent)
            logger.info(f"  ➜ Agent {agent.id} created")
    
    def get_available_agent(self) -> Optional[Agent]:
        """Get available idle agent"""
        for agent in self.agents:
            if agent.status == "idle":
                return agent
        
        # Create new agent if auto_scale enabled
        if self.auto_scale and len(self.agents) < self.max_agents:
            agent = Agent(f"agent_{len(self.agents)}")
            self.agents.append(agent)
            logger.info(f"✨ New agent created: {agent.id}")
            return agent
        
        return None
    
    def get_active_count(self) -> int:
        """Get count of active agents"""
        return len([a for a in self.agents if a.status != "idle"])
    
    def shutdown(self):
        """Shutdown all agents"""
        logger.info("Shutting down agent pool...")
        self.agents.clear()
