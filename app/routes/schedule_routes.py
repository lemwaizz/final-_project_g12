from flask import Blueprint
from app.controllers.schedule_controller import create_schedule, get_schedule

schedule_bp = Blueprint('schedule', __name__)

schedule_bp.route('/schedule', methods=['POST'])(create_schedule)
schedule_bp.route('/schedule', methods=['GET'])(get_schedule)
