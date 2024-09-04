# app/models/class_model.py
class YogaClass:
    @staticmethod
    def get_classes_by_city(conn, city):
        query = "SELECT * FROM yoga_classes WHERE city ILIKE %s;"
        with conn.cursor() as cur:
            cur.execute(query, (city,))
            return cur.fetchall()  # Returns a list of tuples

    @staticmethod
    def add_class(conn, name, instructor, city, time, price):
        query = "INSERT INTO yoga_classes (name, instructor, city, time, price) VALUES (%s, %s, %s, %s, %s) RETURNING id;"
        with conn.cursor() as cur:
            cur.execute(query, (name, instructor, city, time, price))
            class_id = cur.fetchone()[0]
            conn.commit()
            return class_id
