# app/routes/class_routes.py
from flask import Blueprint, request, jsonify
from app.controllers.class_controller import list_classes_by_city, add_class

class_bp = Blueprint('class', __name__)

@class_bp.route('/classes', methods=['GET'])
def list_classes():
    city = request.args.get('city')
    classes = list_classes_by_city(city)
    return jsonify(classes), 200

@class_bp.route('/class', methods=['POST'])
def add():
    data = request.json
    class_id = add_class(data)
    return jsonify({'id': class_id}), 201
