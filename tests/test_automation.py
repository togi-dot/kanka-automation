"""Test automation engine"""

import pytest
from core.automation_engine import AutomationEngine


def test_engine_init():
    """Test engine initialization"""
    config = {
        "llm": {"model": "mistral"},
        "agents": {"max_agents": 5}
    }
    engine = AutomationEngine(config)
    assert engine is not None
    assert engine.running == False


def test_engine_start():
    """Test engine startup"""
    config = {}
    engine = AutomationEngine(config)
    engine.start()
    assert engine.running == True
    engine.shutdown()
    assert engine.running == False
