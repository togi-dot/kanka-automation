"""
Performance Monitor - System metrics and health tracking
"""

import logging
import psutil
from typing import Dict, Any

logger = logging.getLogger(__name__)


class PerformanceMonitor:
    """Monitor system performance"""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.running = False
        logger.info("✅ PerformanceMonitor initialized")
    
    def start(self):
        """Start monitoring"""
        self.running = True
        logger.info("▶️  PerformanceMonitor started")
    
    def stop(self):
        """Stop monitoring"""
        self.running = False
        logger.info("⏹️  PerformanceMonitor stopped")
    
    def get_cpu_usage(self) -> float:
        """Get CPU usage percentage"""
        return psutil.cpu_percent(interval=1)
    
    def get_memory_usage(self) -> float:
        """Get memory usage percentage"""
        return psutil.virtual_memory().percent
