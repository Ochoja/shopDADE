from flask import Blueprint, request
from resources.user_resources import UserListResource, UserResource

user_bp = Blueprint('user', __name__)

# Instantiate user resources
user_list_resource = UserListResource()
user_resource = UserResource()

# Route for getting all users and creating a new user
@user_bp.route('/users', methods=['GET', 'POST'])
def user_list():
    if request.method == 'GET':
        return user_list_resource.get()
    elif request.method == 'POST':
        return user_list_resource.post()

# Routes for getting, updating, and deleting a user by ID
@user_bp.route('/users/<user_id>', methods=['GET', 'PUT', 'DELETE'])
def user_detail(user_id):
    if request.method == 'GET':
        return user_resource.get(user_id)
    elif request.method == 'PUT':
        return user_resource.put(user_id)
    elif request.method == 'DELETE':
        return user_resource.delete(user_id)
