# app/controllers/class_controller.py
from models.class_model import YogaClass
from config.database import get_db_connection

def list_classes_by_city(city):
    conn = get_db_connection()
    classes = YogaClass.get_classes_by_city(conn, city)
    conn.close()
    return classes

def add_class(data):
    conn = get_db_connection()
    class_id = YogaClass.add_class(conn, data['name'], data['instructor'], data['city'], data['time'], data['price'])
    conn.close()
    return class_id
