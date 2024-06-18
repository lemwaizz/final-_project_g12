from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import User
from app.extensions import db

user_bp = Blueprint('user', __name__)

@user_bp.route('/profile', methods=['GET'])
@login_required
def profile():
    user = current_user
    return jsonify({
        'username': user.username,
        'email': user.email,
        'created_at': user.created_at
    })

@user_bp.route('/update', methods=['PUT'])
@login_required
def update_profile():
    data = request.get_json()
    user = current_user
    
    if 'email' in data:
        user.email = data['email']
    if 'password' in data:
        user.set_password(data['password'])
    
    db.session.commit()
    return jsonify({'message': 'Profile updated successfully'})
