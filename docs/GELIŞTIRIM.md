# KANKA Automation - Developer Guide

## Project Structure

```
kanka-automation/
├── core/              # Core engine components
├── agents/            # Agent implementations
├── ai/                # AI/LLM interfaces
├── voice/             # Voice I/O
├── healing/           # Self-healing system
├── monitoring/        # Performance monitoring
├── web/               # Web dashboard
├── apk_builder/       # APK builder
├── database/          # Database layer
├── utils/             # Utilities
└── tests/             # Unit tests
```

## Adding New Components

### 1. Create New Agent

```python
# agents/my_agent.py
from core.agent_pool import Agent

class MyAgent(Agent):
    def __init__(self):
        super().__init__("my_agent")
    
    def execute(self, task):
        # Implement task execution
        return {"status": "success"}
```

### 2. Add Custom Task

```python
# Extend AutomationEngine
from core.automation_engine import AutomationEngine

class CustomEngine(AutomationEngine):
    def run_custom_task(self, params):
        # Custom task logic
        pass
```

### 3. Extend LLM Integration

```python
# In core/llm_manager.py
def custom_endpoint(self, data):
    response = requests.post(
        f"{self.host}/api/custom",
        json=data
    )
    return response.json()
```

## Testing

```bash
# Run tests
pytest tests/

# Run with coverage
pytest --cov=core tests/
```

## Debugging

```python
# Enable debug logging
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Contributing

1. Fork repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request
