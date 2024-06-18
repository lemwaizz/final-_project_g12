import logging
from flask import Flask, render_template
from app.config import Config
from app.extensions import db, login_manager
from app.routes import register_routes

def create_app():
    # Basic logging configuration
    logging.basicConfig(level=logging.DEBUG)
    app = Flask(__name__, static_folder='static', template_folder='templates')
    
    # Configurations
    app.config.from_object(Config)
    
    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    
    # Register routes
    register_routes(app)
    
    @app.route('/test')
    def test():
        return 'This is a test route.'

    app.logger.debug('App created successfully!')
    
    return app
