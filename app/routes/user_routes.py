from flask import Blueprint
from app.controllers.user_controller import profile, update_profile

user_bp = Blueprint('user', __name__)

user_bp.route('/profile', methods=['GET'])(profile)
user_bp.route('/update', methods=['PUT'])(update_profile)
