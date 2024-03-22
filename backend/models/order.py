from database import mongo
from bson.objectid import ObjectId

class Order:
    def __init__(self, user, items, total_price, status="pending", shipping_address=None, payment_details=None):
        self.user = user
        self.items = items
        self.total_price = total_price
        self.status = status
        self.shipping_address = shipping_address
        self.payment_details = payment_details
        self._id = None  # Add _id attribute

    def save(self):
        items_data = []
        for item in self.items:
            item_data = {
                "product": item.product,
                "quantity": item.quantity,
                "price": item.price
            }
            items_data.append(item_data)

        order_data = {
            'user': self.user,
            'items': items_data,
            'total_price': self.total_price,
            'status': self.status,
            'shipping_address': self.shipping_address,
            'payment_details': self.payment_details
        }
        result = mongo.db.orders.insert_one(order_data)
        self._id = result.inserted_id


    @staticmethod
    def find_all():
        orders_cursor = mongo.db.orders.find()
        return orders_cursor


    @staticmethod
    def find_by_id(order_id):
        order = mongo.db.orders.find_one({'_id': ObjectId(order_id)})
        return order


    @staticmethod
    def update_by_id(order_id, update_data):
        mongo.db.orders.update_one({'_id': ObjectId(order_id)}, {'$set': update_data})

    @staticmethod
    def delete_by_id(order_id):
        mongo.db.orders.delete_one({'_id': ObjectId(order_id)})


class OrderItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price
