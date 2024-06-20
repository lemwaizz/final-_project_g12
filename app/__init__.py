# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize SQLAlchemy with the Flask app
    db.init_app(app)

    # Initialize Flask-Migrate with the Flask app and SQLAlchemy db
    migrate.init_app(app, db)

    # Import and register blueprints
    from .routes import auth_bp
    app.register_blueprint(auth_bp)

    return app
