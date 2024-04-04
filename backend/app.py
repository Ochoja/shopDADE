from flask import Flask
from flask_login import LoginManager
from database import init_db
from routes.auth import auth_bp
from routes.user import user_bp
from routes.product import product_bp
from routes.order import order_bp
from routes.category import category_bp
from models.user import User
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Initialize the database
load_dotenv()  # load environment variables
user_name = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
database_uri = f'mongodb+srv://{user_name}:{password}@cluster0.9gfsau1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
init_db(app, database_uri)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Define the user_loader function


@login_manager.user_loader
def load_user(user_id):
    # Load user from the database using the user ID
    return User.query.get(int(user_id))


# Import blueprints and register them
app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)
app.register_blueprint(product_bp)
app.register_blueprint(order_bp)
app.register_blueprint(category_bp)

if __name__ == '__main__':
    app.run(debug=True)
