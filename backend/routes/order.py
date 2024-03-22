from flask import Blueprint, request

from resources.order_resources import OrderListResource, OrderResource

order_bp = Blueprint('order', __name__)

# Instantiate order resources
order_list_resource = OrderListResource()
order_resource = OrderResource()

# Route for getting all orders and creating a new order
@order_bp.route('/orders', methods=['GET', 'POST'])
def orders():
    if request.method == 'GET':
        return order_list_resource.get()
    elif request.method == 'POST':
        return order_list_resource.post()

# Routes for getting, updating, and deleting an order by ID
@order_bp.route('/orders/<order_id>', methods=['GET', 'PUT', 'DELETE'])
def order(order_id):
    if request.method == 'GET':
        return order_resource.get(order_id)
    elif request.method == 'PUT':
        return order_resource.put(order_id)
    elif request.method == 'DELETE':
        return order_resource.delete(order_id)
