# app/__init__.py

from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from .routes import register_blueprints

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize SQLAlchemy with the Flask app
    db.init_app(app)

    # Import and register blueprints
    from .routes import auth_bp
    app.register_blueprint(auth_bp)

    return app
