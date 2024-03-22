from flask_restful import Resource
from flask import request, jsonify
from models.user import User
from database import mongo
from bson import ObjectId


class UserListResource(Resource):
    def get(self):
        users = list(mongo.db.users.find())
        # Convert ObjectId to string for each user
        users_json = []
        for user in users:
            user['_id'] = str(user['_id'])
            users_json.append(user)
        return {'users': users_json}

    def post(self):
        data = request.get_json()
        existing_email_user = User.find_by_email(data['email'])
        existing_fullname_user = User.find_by_fullname(data['fullname'])
        if existing_email_user:
            return {'error': 'Email already exists'}, 400
        if existing_fullname_user:
            return {'error': 'fullname already exists'}, 400
        user = User(**data).save()
        return {'id': str(user.id)}, 201

class UserResource(Resource):
    def get(self, user_id):
        user = mongo.db.users.find_one({'_id': ObjectId(user_id)})
        if user:
            user['_id'] = str(user['_id'])  # Convert ObjectId to string
            return jsonify({'user': user}), 200
        else:
            return {'message': 'User not found'}, 404

    def put(self, user_id):
        data = request.get_json()
        if not data:
            return {'message': 'No data provided for update'}, 400

        updated_user = User.update_by_id(user_id, data)
        if updated_user:
            updated_user['_id'] = str(updated_user['_id'])  # Convert ObjectId to string
            return {'message': 'User updated successfully', 'user': updated_user}, 200
        else:
            return {'message': 'User not found'}, 404



    def delete(self, user_id):
        result = User.delete_by_id(user_id)
        if result.deleted_count > 0:
            return {'message': 'User deleted successfully'}, 200
        else:
            return {'message': 'User not found'}, 404
