from flask_restful import Resource
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
from flask_jwt_extended import create_access_token

class UserRegistration(Resource):
    def post(self):
        data = request.get_json()
        # Check if fullname or email already exists
        if User.objects(fullname=data['fullname']).first() or User.objects(email=data['email']).first():
            return {'message': 'fullname or email already exists'}, 400

        hashed_password = generate_password_hash(data['password'], method='sha256')
        new_user = User(fullname=data['fullname'], email=data['email'], password=hashed_password)
        new_user.save()
        access_token = create_access_token(identity=data['fullname'])
        return {'message': 'User {} created successfully'.format(data['fullname']), 'access_token': access_token}, 201

class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        user = User.objects(fullname=data['fullname']).first()
        if user and check_password_hash(user.password, data['password']):
            access_token = create_access_token(identity=data['fullname'])
            return {'message': 'Logged in as {}'.format(user.fullname), 'access_token': access_token}, 200
        else:
            return {'message': 'Invalid credentials'}, 401
