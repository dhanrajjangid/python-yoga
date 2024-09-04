from flask import Blueprint, request, jsonify
from app.controllers.class_controller import list_classes_by_city, add_class

class_bp = Blueprint('class', __name__)

@class_bp.route('/classes', methods=['GET'])
def list_classes():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400
    classes = list_classes_by_city(city)
    return jsonify(classes), 200

@class_bp.route('/class', methods=['POST'])
def add():
    data = request.json
    required_fields = ['name', 'instructor', 'city', 'time', 'price']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    class_id = add_class(data)
    return jsonify({'id': class_id}), 201
