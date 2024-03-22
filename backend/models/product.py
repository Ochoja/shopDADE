from flask import app
from database import mongo
from bson.objectid import ObjectId  # Import ObjectId for generating _id
import os
from werkzeug.utils import secure_filename

class Product:
    def __init__(self, name, price, old_price=None, description=None, category=None, image_url=None, image_file=None, sizes=None, image_base64=None):
        self.name = name
        self.price = price
        self.old_price = old_price
        self.description = description
        self.category = category
        self.image_url = image_url
        self.image_file = image_file
        self.sizes = sizes
        self.image_base64 = image_base64  # Add image_base64 field

    def save(self):
        product_data = {
            'name': self.name,
            'price': self.price,
            'old_price': self.old_price,
            'description': self.description,
            'category': self.category,
            'image_url': self.image_url,
            'sizes': self.sizes,
            'image_base64': self.image_base64  # Include image_base64 in saved data
        }
        # Insert the product data and get the inserted ID
        inserted_id = mongo.db.products.insert_one(product_data).inserted_id
        # Assign the generated ID to the object
        self._id = inserted_id

        # Save the uploaded image file
        if self.image_file:
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(self.image_file.filename))
            self.image_file.save(image_path)

    @staticmethod
    def find_all():
        return list(mongo.db.products.find())

    @staticmethod
    def find_by_id(product_id):
        return mongo.db.products.find_one({'_id': ObjectId(product_id)})

    @staticmethod
    def update_by_id(product_id, update_data):
        mongo.db.products.update_one({'_id': ObjectId(product_id)}, {'$set': update_data})

    @staticmethod
    def delete_by_id(product_id):
        mongo.db.products.delete_one({'_id': ObjectId(product_id)})

    @staticmethod
    def find_by_name(name):
        return mongo.db.products.find_one({'name': name})
