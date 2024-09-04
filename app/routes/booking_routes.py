# app/routes/booking_routes.py
from flask import Blueprint, request, jsonify
from app.controllers.booking_controller import create_booking, get_user_bookings

booking_bp = Blueprint('booking', __name__)

@booking_bp.route('/booking', methods=['POST'])
def book_class():
    data = request.json
    booking_id = create_booking(data)
    return jsonify({'id': booking_id}), 201

@booking_bp.route('/bookings/<int:user_id>', methods=['GET'])
def list_user_bookings(user_id):
    bookings = get_user_bookings(user_id)
    return jsonify(bookings), 200
