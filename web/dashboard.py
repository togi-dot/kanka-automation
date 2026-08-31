"""
Web Dashboard
"""

import logging
from flask import Flask, render_template, jsonify

logger = logging.getLogger(__name__)


def start_dashboard(engine):
    """Start web dashboard"""
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        return "KANKA Automation Dashboard"
    
    @app.route('/api/status')
    def get_status():
        return jsonify(engine.get_status())
    
    logger.info("🌐 Starting dashboard on http://localhost:8000")
    app.run(host='0.0.0.0', port=8000, debug=False)
