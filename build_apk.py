#!/usr/bin/env python3
"""APK Builder"""

import sys
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from core.automation_engine import AutomationEngine


def main():
    """Build APK"""
    parser = argparse.ArgumentParser(description="KANKA APK Builder")
    parser.add_argument('--app', type=str, default='kanka-app', help='App name')
    args = parser.parse_args()
    
    print("""
╔══════════════════════════════════════════════════════════════╗
║        📱 KANKA APK BUILDER v1.0.0                         ║
║   APK İnşa Aracı - APK Builder                              ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    try:
        engine = AutomationEngine()
        apk_path = engine.build_apk(args.app)
        print(f"✅ APK built: {apk_path}")
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
