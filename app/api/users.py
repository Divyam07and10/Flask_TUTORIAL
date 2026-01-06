from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from pydantic import ValidationError
from app.schemas.user_schema import UserUpdateSchema, UserResponseSchema
from app.services import user_service as service

users_bp = Blueprint('users', __name__)

@users_bp.route('/', methods=['GET'])
@jwt_required()
def list_users():
    users = service.get_all_users()
    return jsonify([UserResponseSchema.model_validate(u).model_dump() for u in users]), 200

@users_bp.route('/me', methods=['GET'])
@jwt_required()
def get_me():
    user_id = get_jwt_identity()
    user = service.get_user(user_id)
    if not user:
        return jsonify({"msg": "User not found"}), 404
    return jsonify(UserResponseSchema.model_validate(user).model_dump()), 200

@users_bp.route('/<string:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    user = service.get_user(user_id)
    if not user:
        return jsonify({"msg": "User not found"}), 404
    return jsonify(UserResponseSchema.model_validate(user).model_dump()), 200

@users_bp.route('/<string:user_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_user(user_id):
    user = service.get_user(user_id)
    if not user:
        return jsonify({"msg": "User not found"}), 404
    
    try:
        data = UserUpdateSchema(**request.json)
        updated_user = service.update_user(user, data)
    except ValidationError as e:
        return jsonify(e.errors()), 400
    except ValueError as e:
        return jsonify({"msg": str(e)}), 400
        
    return jsonify(UserResponseSchema.model_validate(updated_user).model_dump()), 200

@users_bp.route('/<string:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    user = service.get_user(user_id)
    if not user:
        return jsonify({"msg": "User not found"}), 404
    
    service.delete_user(user)
    return jsonify({"msg": "User deleted successfully"}), 200
