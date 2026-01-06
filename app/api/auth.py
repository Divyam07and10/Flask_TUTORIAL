from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from app.schemas.user_schema import UserCreateSchema
from app.services import user_service as service
from app.core.security import verify_password
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        data = UserCreateSchema(**request.json)
    except ValidationError as e:
        return jsonify(e.errors()), 400

    if service.get_by_username(data.username):
        return jsonify({"msg": "Username already exists"}), 400
    
    user = service.create_user(data)
    return jsonify({"msg": "User created successfully", "id": user.id}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = service.get_by_username(username)
    if user and verify_password(password, user.password_hash):
        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)
        return jsonify(access_token=access_token, refresh_token=refresh_token), 200
        
    return jsonify({"msg": "Invalid username or password"}), 401

@auth_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return jsonify(access_token=access_token), 200
