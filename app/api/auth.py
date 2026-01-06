from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from app.schemas.user_schema import UserCreateSchema
from app.services import user_service as service
from app.core.security import verify_password
from flask_jwt_extended import (
    create_access_token, 
    create_refresh_token, 
    jwt_required, 
    get_jwt_identity,
    set_access_cookies,
    set_refresh_cookies,
    unset_jwt_cookies,
    get_csrf_token
)

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
    return jsonify({"msg": "User created successfully Please login to continue", "id": user.id}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = service.get_by_username(username)
    if user and verify_password(password, user.password_hash):
        access_token = create_access_token(identity=str(user.id))
        refresh_token = create_refresh_token(identity=str(user.id))
        
        response = jsonify({
            "msg": "Login successful",
            "access_csrf": get_csrf_token(access_token),
            "refresh_csrf": get_csrf_token(refresh_token)
        })
        set_access_cookies(response, access_token)
        set_refresh_cookies(response, refresh_token)
        return response, 200
        
    return jsonify({"msg": "Invalid username or password"}), 401

@auth_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    response = jsonify({
        "msg": "Token refreshed",
        "access_csrf": get_csrf_token(access_token)
    })
    set_access_cookies(response, access_token)
    return response, 200

@auth_bp.route('/logout', methods=['POST'])
def logout():
    response = jsonify({"msg": "Successfully logged out"})
    unset_jwt_cookies(response)
    return response, 200
