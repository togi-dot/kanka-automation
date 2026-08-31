#!/usr/bin/env python3
"""Agent Pool Management"""

import logging
import uuid

logger = logging.getLogger(__name__)


class Agent:
    """Individual Agent"""
    
    def __init__(self, agent_type="default"):
        self.id = str(uuid.uuid4())[:8]
        self.type = agent_type
        self.status = "idle"
        self.tasks = []
    
    def execute(self, task):
        """Execute task"""
        self.status = "busy"
        logger.info(f"Agent {self.id} executing: {task}")
        self.status = "idle"
        return {"status": "completed"}


class AgentPool:
    """Manages pool of agents"""
    
    def __init__(self, config=None):
        self.config = config or {}
        self.agents = []
        self.max_agents = self.config.get('max_agents', 5)
        self._init_agents()
    
    def _init_agents(self):
        """Initialize agent pool"""
        for i in range(self.max_agents):
            agent = Agent(f"worker-{i}")
            self.agents.append(agent)
            logger.info(f"✅ Agent {agent.id} created")
    
    def get_available_agent(self):
        """Get available idle agent"""
        for agent in self.agents:
            if agent.status == "idle":
                return agent
        return None
    
    def get_active_count(self):
        """Get count of active agents"""
        return sum(1 for a in self.agents if a.status == "busy")
