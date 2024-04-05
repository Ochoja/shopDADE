from flask import Blueprint, request, jsonify, redirect, url_for
from flask_login import logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    fullname = data.get('fullname')
    email = data.get('email')
    password = data.get('password')
    name = data.get('name')
    address = data.get('address')
    phone_number = data.get('phone_number')

    # Check if fullname or email already exists
    if User.find_by_email(email) or User.find_by_fullname(fullname):
        return jsonify({'message': 'fullname or email already exists'}), 400

    # Hash the password before saving
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

    # Create a new user instance and save to the database
    new_user = User(fullname=fullname, email=email, password=hashed_password,
                    name=name, address=address, phone_number=phone_number)
    new_user.save()

    return jsonify({'message': 'User created successfully'}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    # Find the user by email
    user = User.find_by_email(email)

    # Check if the user exists and the password is correct
    if user and check_password_hash(user['password'], password):
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401


@auth_bp.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()  # This assumes Flask-Login is properly initialized
    return redirect(url_for('auth.login'))
