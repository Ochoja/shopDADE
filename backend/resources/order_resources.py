from flask_restful import Resource, reqparse
from flask import jsonify
from models.order import Order, OrderItem
from models.user import User
from models.product import Product
from bson import json_util
from schemas import OrderSchema  # Import the schema for Order

order_schema = OrderSchema()  # Initialize the schema

class OrderListResource(Resource):
    def get(self):
        orders_cursor = Order.find_all()
        serialized_orders = [order_schema.dump(order) for order in orders_cursor]
        return jsonify(serialized_orders)


    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=str, required=True)
        parser.add_argument('items', type=dict, action='append', required=True)
        parser.add_argument('total_price', type=float, required=True)
        parser.add_argument('status', type=str, default='pending')
        parser.add_argument('shipping_address', type=str)
        parser.add_argument('payment_details', type=str)
        args = parser.parse_args()

        user_id = args.pop('user_id')
        user = User.find_by_id(user_id)

        items_data = args.pop('items')
        items = []
        for item_data in items_data:
            product_id = item_data.pop('product_id')
            product = Product.find_by_id(product_id)
            item_data['product'] = product
            items.append(OrderItem(**item_data))

        order = Order(user=user, items=items, **args)
        order.save()
        return {'id': str(order._id)}, 201


class OrderResource(Resource):
    def get(self, order_id):
        order = Order.find_by_id(order_id)
        if order:
            # Convert ObjectId to string using json_util
            order_json = json_util.dumps(order)
            return order_json, 200
        else:
            return {'message': 'Order not found'}, 404

    def put(self, order_id):
        parser = reqparse.RequestParser()
        parser.add_argument('status', type=str)
        args = parser.parse_args()

        Order.update_by_id(order_id, args)
        return {'message': 'Order updated successfully'}, 200

    def delete(self, order_id):
        Order.delete_by_id(order_id)
        return {'message': 'Order deleted successfully'}, 200
