# app/controllers/user_controller.py
from models.user_model import User
from config.database import get_db_connection

def register_user(data):
    conn = get_db_connection()
    user_id = User.create_user(conn, data['username'], data['password'])
    conn.close()
    return user_id

def get_user(user_id):
    conn = get_db_connection()
    user = User.get_user_by_id(conn, user_id)
    conn.close()
    return user
