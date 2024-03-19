from flask import Blueprint, request

from resources.product_resources import ProductListResource, ProductResource

product_bp = Blueprint('product', __name__)

# Instantiate product resources
product_list_resource = ProductListResource()
product_resource = ProductResource()

# Route for getting all products and creating a new product
@product_bp.route('/products', methods=['GET', 'POST'])
def products():
    if request.method == 'GET':
        return product_list_resource.get()
    elif request.method == 'POST':
        return product_list_resource.post()

# Routes for getting, updating, and deleting a product by ID
@product_bp.route('/products/<product_id>', methods=['GET', 'PUT', 'DELETE'])
def product(product_id):
    if request.method == 'GET':
        return product_resource.get(product_id)
    elif request.method == 'PUT':
        return product_resource.put(product_id)
    elif request.method == 'DELETE':
        return product_resource.delete(product_id)
