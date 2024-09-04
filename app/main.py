# app/main.py
from flask import Flask
from app.routes.user_routes import user_bp
from app.routes.class_routes import class_bp
from app.routes.booking_routes import booking_bp

app = Flask(__name__)

app.register_blueprint(user_bp)
app.register_blueprint(class_bp)
app.register_blueprint(booking_bp)

if __name__ == '__main__':
    app.run(debug=True)
