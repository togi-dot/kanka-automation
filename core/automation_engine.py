#!/usr/bin/env python3
"""Core Automation Engine"""

import logging
import sys
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class AutomationEngine:
    """Main automation engine"""
    
    def __init__(self, config=None):
        self.config = config or {}
        self.running = False
        self.agents = []
        self.tasks = []
        logger.info("✅ AutomationEngine initialized")
    
    def start(self):
        """Start the engine"""
        self.running = True
        logger.info("🚀 Engine started")
        return True
    
    def shutdown(self):
        """Shutdown the engine"""
        self.running = False
        logger.info("⛔ Engine stopped")
        return True
    
    def run_task(self, task_desc):
        """Run a task"""
        logger.info(f"📋 Running task: {task_desc}")
        return {"status": "success", "task": task_desc}
    
    def start_voice_controller(self):
        """Start voice command mode"""
        logger.info("🎤 Voice controller started")
        self.start()
        print("\n" + "="*50)
        print("🎤 VOICE CONTROLLER ACTIVE")
        print("Say 'help' for commands")
        print("="*50 + "\n")
        
        while self.running:
            try:
                cmd = input("\n🎤 Command: ").strip().lower()
                if cmd in ['exit', 'quit', 'stop']:
                    logger.info("Voice controller stopped")
                    self.shutdown()
                    break
                elif cmd == 'help':
                    print("""
Available commands:
  - status: Show system status
  - start: Start automation
  - stop: Stop automation
  - task [desc]: Run a task
  - agents: List active agents
  - help: Show this help
  - exit: Exit voice mode
""")
                elif cmd == 'status':
                    print(f"Status: {'Running' if self.running else 'Stopped'}")
                elif cmd == 'agents':
                    print(f"Active agents: {len(self.agents)}")
                elif cmd.startswith('task '):
                    task = cmd[5:]
                    result = self.run_task(task)
                    print(f"✅ Task result: {result}")
                else:
                    print("Unknown command. Type 'help' for commands.")
            except KeyboardInterrupt:
                logger.info("Voice controller interrupted")
                self.shutdown()
                break
            except Exception as e:
                logger.error(f"Error: {e}")
    
    def start_web_dashboard(self):
        """Start web dashboard"""
        logger.info("🌐 Starting web dashboard on http://localhost:8000")
        try:
            from flask import Flask, jsonify
            app = Flask(__name__)
            
            @app.route('/')
            def home():
                return jsonify({
                    "app": "KANKA AUTOMATION",
                    "version": "1.0.0",
                    "status": "running",
                    "timestamp": datetime.now().isoformat()
                })
            
            @app.route('/api/status')
            def status():
                return jsonify({
                    "engine_running": self.running,
                    "agents_count": len(self.agents),
                    "tasks_count": len(self.tasks)
                })
            
            @app.route('/api/start', methods=['POST'])
            def api_start():
                self.start()
                return jsonify({"status": "started"})
            
            @app.route('/api/stop', methods=['POST'])
            def api_stop():
                self.shutdown()
                return jsonify({"status": "stopped"})
            
            print("\n" + "="*50)
            print("🌐 WEB DASHBOARD")
            print("http://localhost:8000")
            print("="*50 + "\n")
            
            app.run(host='0.0.0.0', port=8000, debug=False)
        except Exception as e:
            logger.error(f"Dashboard error: {e}")
    
    def build_apk(self, app_name):
        """Build APK"""
        logger.info(f"📱 Building APK: {app_name}")
        return f"/build/{app_name}.apk"
    
    def get_status(self):
        """Get system status"""
        return {
            "running": self.running,
            "agents": len(self.agents),
            "tasks": len(self.tasks),
            "timestamp": datetime.now().isoformat()
        }
