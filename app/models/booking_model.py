# app/models/booking_model.py
class Booking:
    @staticmethod
    def create_booking(conn, user_id, class_id, date):
        query = "INSERT INTO bookings (user_id, class_id, date) VALUES (%s, %s, %s) RETURNING id;"
        with conn.cursor() as cur:
            cur.execute(query, (user_id, class_id, date))
            booking_id = cur.fetchone()['id']
            conn.commit()
            return booking_id

    @staticmethod
    def get_user_bookings(conn, user_id):
        query = "SELECT * FROM bookings WHERE user_id = %s;"
        with conn.cursor() as cur:
            cur.execute(query, (user_id,))
            return cur.fetchall()
