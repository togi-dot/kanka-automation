"""
Database Manager - SQLite local database
"""

import logging
import sqlite3
from typing import Dict, Any
from pathlib import Path

logger = logging.getLogger(__name__)


class DatabaseManager:
    """Manage SQLite database"""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.db_path = self.config.get("path", "./data/kanka.db")
        
        # Create data directory
        Path(self.db_path).parent.mkdir(parents=True, exist_ok=True)
        
        self.conn = None
        self._init_db()
        logger.info(f"✅ DatabaseManager initialized at {self.db_path}")
    
    def _init_db(self):
        """Initialize database"""
        try:
            self.conn = sqlite3.connect(self.db_path)
            self.conn.execute("SELECT 1")
            logger.info("✅ Database connection successful")
        except Exception as e:
            logger.error(f"Database error: {e}")
    
    def close(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()
            logger.info("✅ Database closed")
