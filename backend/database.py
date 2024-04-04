from flask_pymongo import PyMongo

mongo = PyMongo()


def init_db(app, uri):
    app.config['MONGO_URI'] = uri  # Update with your MongoDB URI
    mongo.init_app(app)
