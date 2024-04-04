from database import mongo
from bson.objectid import ObjectId  # Import ObjectId for generating _id

class Product:
    def __init__(self, title, price, old_price=None, description=None, stock_quantity=0, category_id=None, image_url=None):
        self.title = title
        self.description = description
        self.price = price
        self.old_price = old_price
        self.stock_quantity = stock_quantity
        self.category_id = category_id
        self.image_url = image_url
        # Add more fields as needed

    def save(self):
        product_data = {
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'old_price': self.old_price,
            'stock_quantity': self.stock_quantity,
            'category_id': self.category_id,  # Corrected field name
            'image_url': self.image_url
        }
        # Insert the product data and get the inserted ID
        inserted_id = mongo.db.products.insert_one(product_data).inserted_id
        # Assign the generated ID to the object
        self._id = inserted_id

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
    def find_by_title(title):
        return mongo.db.products.find_one({'title': title})
