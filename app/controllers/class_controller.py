from app.models.class_model import YogaClass
from app.config.database import get_db_connection

def list_classes_by_city(city):
    conn = get_db_connection()
    try:
        classes = YogaClass.get_classes_by_city(conn, city)
    finally:
        conn.close()
    return classes

def add_class(data):
    conn = get_db_connection()
    try:
        class_id = YogaClass.add_class(conn, data['name'], data['instructor'], data['city'], data['time'], data['price'])
    finally:
        conn.close()
    return class_id
