#!/usr/bin/env python3
"""Voice Command Controller"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from core.automation_engine import AutomationEngine


def main():
    """Start voice controller"""
    print("""
╔══════════════════════════════════════════════════════════════╗
║        🎤 KANKA VOICE CONTROLLER v1.0.0                    ║
║   Sesli Komut - Voice Commands                              ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    try:
        engine = AutomationEngine()
        engine.start_voice_controller()
    except KeyboardInterrupt:
        print("\n⛔ Voice controller stopped")
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
