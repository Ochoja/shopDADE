from database import mongo
from bson.objectid import ObjectId

class User:
    def __init__(self, username, email, password, name, address=None, phone_number=None):
        self.username = username
        self.email = email
        self.password = password
        self.name = name
        self.address = address
        self.phone_number = phone_number

    def save(self):
        user_data = {
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'name': self.name,
            'address': self.address,
            'phone_number': self.phone_number
        }
        return mongo.db.users.insert_one(user_data)

    @staticmethod
    def find_by_email(email):
        return mongo.db.users.find_one({'email': email})

    @staticmethod
    def find_by_username(username):
        return mongo.db.users.find_one({'username': username})

    @staticmethod
    def find_by_id(user_id):
        return mongo.db.users.find_one({'_id': user_id})

    @staticmethod
    def update_by_id(user_id, update_data):
        update_data.pop('_id', None)
        result = mongo.db.users.update_one({'_id': ObjectId(user_id)}, {'$set': update_data})
        if result.modified_count > 0:
            return mongo.db.users.find_one({'_id': ObjectId(user_id)})  # Return the updated user document
        else:
            return None  # Return None if user was not found or not modified


    @staticmethod
    def delete_by_id(user_id):
        return mongo.db.users.delete_one({'_id': ObjectId(user_id)})
