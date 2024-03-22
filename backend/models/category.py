from database import mongo
from bson.objectid import ObjectId

class Category:
    def __init__(self, name, description=None):
        self.name = name
        self.description = description
        self._id = None  # Initialize _id attribute

    def save(self):
        existing_category = self.find_by_name(self.name)
        if existing_category:
            raise ValueError("Category with this name already exists")
        result = mongo.db.categories.insert_one({
            'name': self.name,
            'description': self.description
        })
        self._id = result.inserted_id  # Assign the inserted _id to the object

    def update_by_id(self, category_id, new_name, new_description):
        mongo.db.categories.update_one(
            {'_id': ObjectId(category_id)},
            {'$set': {'name': new_name, 'description': new_description}}
        )

    @staticmethod
    def find_all():
        categories = list(mongo.db.categories.find())
        for category in categories:
            category['_id'] = str(category['_id'])  # Convert ObjectId to string
        return categories

    @staticmethod
    def find_by_id(category_id):
        return mongo.db.categories.find_one({'_id': ObjectId(category_id)})

    @staticmethod
    def delete_by_id(category_id):
        mongo.db.categories.delete_one({'_id': ObjectId(category_id)})

    @staticmethod
    def find_by_name(name):
        return mongo.db.categories.find_one({'name': name})

    @staticmethod
    def delete_by_name(name):
        mongo.db.categories.delete_one({'name': name})
