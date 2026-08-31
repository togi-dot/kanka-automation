#!/usr/bin/env python3
"""
Web Dashboard Launcher
"""

import sys
import logging
from pathlib import Path
import yaml

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

sys.path.insert(0, str(Path(__file__).parent))

from core.automation_engine import AutomationEngine


def main():
    """Start web dashboard"""
    print("""
╔══════════════════════════════════════════════════════════════╗
║        🌐 KANKA WEB DASHBOARD v1.0.0                       ║
║   Web Arayüzü - Web Interface                               ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    try:
        # Load configuration
        with open('config.yaml', 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        
        logger.info("✅ Configuration loaded")
        
        # Initialize engine
        engine = AutomationEngine(config)
        
        # Start web dashboard
        logger.info("🌐 Starting web dashboard...")
        engine.start_web_dashboard()
        
    except KeyboardInterrupt:
        logger.info("\n⛔ Dashboard stopped by user")
    except Exception as e:
        logger.error(f"❌ Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
