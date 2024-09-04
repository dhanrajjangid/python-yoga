# app/routes/user_routes.py
from flask import Blueprint, request, jsonify
from controllers.user_controller import register_user, get_user

user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    user_id = register_user(data)
    return jsonify({'id': user_id}), 201

@user_bp.route('/user/<int:id>', methods=['GET'])
def get(id):
    user = get_user(id)
    return jsonify(user), 200
