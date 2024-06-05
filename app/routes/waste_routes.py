from flask import Blueprint, request, jsonify
from app import db
from app.models import WasteCollection, Recycling
from flask_login import current_user, login_required

waste_bp = Blueprint('waste', __name__)

@waste_bp.route('/schedule', methods=['POST'])
@login_required
def schedule_waste_collection():
    """
    Schedules a waste collection.
    Expects JSON data: {'schedule': <datetime>, 'status': 'scheduled'}
    """
    data = request.get_json()
    collection = WasteCollection(user_id=current_user.id, schedule=data['schedule'], status='scheduled')
    db.session.add(collection)
    db.session.commit()
    return jsonify({'message': 'Waste collection scheduled successfully'})

@waste_bp.route('/collections', methods=['GET'])
@login_required
def get_waste_collections():
    """
    Retrieves all waste collections for the logged-in user.
    """
    collections = WasteCollection.query.filter_by(user_id=current_user.id).all()
    return jsonify([{
        'id': c.id,
        'schedule': c.schedule,
        'status': c.status
    } for c in collections])

@waste_bp.route('/recycle', methods=['POST'])
@login_required
def log_recycling():
    """
    Logs a recycling effort.
    Expects JSON data: {'weight': <float>}
    """
    data = request.get_json()
    recycling = Recycling(user_id=current_user.id, weight=data['weight'])
    db.session.add(recycling)
    db.session.commit()
    return jsonify({'message': 'Recycling logged successfully'})

@waste_bp.route('/recycling', methods=['GET'])
@login_required
def get_recycling_logs():
    """
    Retrieves all recycling logs for the logged-in user.
    """
    recycling_logs = Recycling.query.filter_by(user_id=current_user.id).all()
    return jsonify([{
        'id': r.id,
        'date': r.date,
        'weight': r.weight
    } for r in recycling_logs])

