# app/models/user_model.py
class User:
    @staticmethod
    def create_user(conn, username, password):
        query = "INSERT INTO users (username, password) VALUES (%s, %s) RETURNING id;"
        with conn.cursor() as cur:
            cur.execute(query, (username, password))
            user_id = cur.fetchone()['id']
            conn.commit()
            return user_id
        

    @staticmethod
    def get_user_by_id(conn, user_id):
        query = "SELECT * FROM users WHERE id = %s;"
        with conn.cursor() as cur:
            cur.execute(query, (user_id,))
            return cur.fetchone()
