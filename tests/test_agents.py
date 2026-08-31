"""Test agent pool"""

import pytest
from core.agent_pool import Agent, AgentPool


def test_agent_creation():
    """Test agent creation"""
    agent = Agent("test")
    assert agent.id is not None
    assert agent.type == "test"
    assert agent.status == "idle"


def test_agent_pool():
    """Test agent pool"""
    config = {"max_agents": 5, "auto_scale": True}
    pool = AgentPool(config)
    assert len(pool.agents) > 0
    
    agent = pool.get_available_agent()
    assert agent is not None
