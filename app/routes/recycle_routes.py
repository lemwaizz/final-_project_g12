from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from app.models import Recycling
from app.extensions import db

recycle_bp = Blueprint('recycle', __name__)

@recycle_bp.route('/recycle', methods=['POST'])
@login_required
def track_recycle():
    data = request.get_json()
    recycle = Recycling(
        user_id=current_user.id,
        item=data['item'],
        quantity=data['quantity'],
        date=data['date']
    )
    db.session.add(recycle)
    db.session.commit()
    return jsonify({'message': 'Recycling effort tracked successfully'})

@recycle_bp.route('/recycle', methods=['GET'])
@login_required
def get_recycle():
    recycling_records = Recycling.query.filter_by(user_id=current_user.id).all()
    return jsonify([{
        'id': record.id,
        'item': record.item,
        'quantity': record.quantity,
        'date': record.date
    } for record in recycling_records])
