from flask import Blueprint
from app.controllers.recycle_controller import track_recycle, get_recycle

recycle_bp = Blueprint('recycle', __name__)

recycle_bp.route('/recycle', methods=['POST'])(track_recycle)
recycle_bp.route('/recycle', methods=['GET'])(get_recycle)
