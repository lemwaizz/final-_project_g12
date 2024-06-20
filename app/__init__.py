import os
from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy

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

if __name__ == "__main__":
    # Use the PORT environment variable if provided, otherwise default to 5000
    port = int(os.environ.get("PORT", 5000))
    app = create_app()
    app.run(host='0.0.0.0', port=port)
