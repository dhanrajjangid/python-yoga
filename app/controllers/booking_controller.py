# app/controllers/booking_controller.py
from app.models.booking_model import Booking
from app.config.database import get_db_connection

def create_booking(data):
    conn = get_db_connection()
    booking_id = Booking.create_booking(conn, data['user_id'], data['class_id'], data['date'])
    conn.close()
    return booking_id

def get_user_bookings(user_id):
    conn = get_db_connection()
    bookings = Booking.get_user_bookings(conn, user_id)
    conn.close()
    return bookings
