# KANKA Automation - API Documentation

## AutomationEngine

### Initialization

```python
from core.automation_engine import AutomationEngine

config = {
    "llm": {"model": "mistral"},
    "agents": {"max_agents": 5}
}

engine = AutomationEngine(config)
```

### Methods

#### start()
Start the automation engine.

```python
engine.start()
```

#### shutdown()
Shutdown the automation engine.

```python
engine.shutdown()
```

#### run_task(task_description: str)
Run an automation task.

```python
result = engine.run_task("Create a Python script")
print(result)  # {"status": "success", ...}
```

#### start_voice_controller()
Start interactive voice command mode.

```python
engine.start_voice_controller()
```

#### start_web_dashboard()
Start web dashboard on http://localhost:8000.

```python
engine.start_web_dashboard()
```

#### build_apk(app_name: str)
Build an APK application.

```python
apk_path = engine.build_apk("my-app")
```

#### get_status()
Get current system status.

```python
status = engine.get_status()
print(status)  # {"running": True, "cpu": 25.5, ...}
```

## AgentPool

### Methods

#### get_available_agent()
Get an idle agent from the pool.

```python
from core.agent_pool import AgentPool

pool = AgentPool()
agent = pool.get_available_agent()
```

#### get_active_count()
Get count of active agents.

```python
active = pool.get_active_count()
```

## LLMManager

### Methods

#### generate_response(prompt: str)
Generate response from LLM.

```python
from core.llm_manager import LLMManager

llm = LLMManager()
response = llm.generate_response("What is Python?")
```

#### generate_plan(task: str)
Generate execution plan for a task.

```python
plan = llm.generate_plan("Build a web app")
```
