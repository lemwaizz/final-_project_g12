from flask import Blueprint, request, jsonify, redirect, url_for
#from app import db
from app.models import User
from app.forms import LoginForm, RegistrationForm
from flask_login import login_user, logout_user, login_required

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Handles user login.
    Expects JSON data: {'username': <username>, 'password': <password>}
    """
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user is None or not user.check_password(data['password']):
        return jsonify({'error': 'Invalid username or password'}), 401
    login_user(user)
    return jsonify({'message': 'Login successful'})

@auth_bp.route('/register', methods=['POST'])
def register():
    """
    Handles user registration.
    Expects JSON data: {'username': <username>, 'email': <email>, 'password': <password>}
    """
    data = request.get_json()
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'error': 'Username already exists'}), 400
    user = User(username=data['username'], email=data['email'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'Registration successful'}), 201

@auth_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    """
    Handles user logout.
    """
    logout_user()
    return jsonify({'message': 'Logout successful'})

