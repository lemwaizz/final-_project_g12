from flask import request, jsonify
from flask_login import login_required, current_user
from app.models import Schedule
from app.extensions import db

@login_required
def create_schedule():
    data = request.get_json()
    schedule = Schedule(
        user_id=current_user.id,
        date=data['date'],
        time=data['time']
    )
    db.session.add(schedule)
    db.session.commit()
    return jsonify({'message': 'Schedule created successfully'})

@login_required
def get_schedule():
    schedules = Schedule.query.filter_by(user_id=current_user.id).all()
    return jsonify([{
        'id': schedule.id,
        'date': schedule.date,
        'time': schedule.time
    } for schedule in schedules])
