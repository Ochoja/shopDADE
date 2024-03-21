from flask import Flask
from flask_login import LoginManager
from database import init_db
from routes.auth import auth_bp
from routes.user import user_bp
from routes.product import product_bp
from models.user import User

app = Flask(__name__)

# Initialize the database
init_db(app)

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

if __name__ == '__main__':
    app.run(debug=True)
