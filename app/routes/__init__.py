from flask import Blueprint
from .auth import auth_bp
from .user import user_bp
from .schedule import schedule_bp
from .recycle import recycle_bp

def register_routes(app):
    from app.routes.auth_routes import auth_bp
    from app.routes.user_routes import user_bp
    from app.routes.schedule_routes import schedule_bp
    from app.routes.recycle_routes import recycle_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(schedule_bp, url_prefix='/api/schedules')
    app.register_blueprint(recycle_bp, url_prefix='/api/recycle')
