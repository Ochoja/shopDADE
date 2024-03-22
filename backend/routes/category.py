from flask import Blueprint, request

from resources.category_resources import CategoryListResource, CategoryResource

category_bp = Blueprint('category', __name__)

# Instantiate category resources
category_list_resource = CategoryListResource()
category_resource = CategoryResource()

# Route for getting all categories and creating a new category
@category_bp.route('/categories', methods=['GET', 'POST'])
def categories():
    if request.method == 'GET':
        return category_list_resource.get()
    elif request.method == 'POST':
        return category_list_resource.post()

# Routes for getting, updating, and deleting a category by ID
@category_bp.route('/categories/<category_id>', methods=['GET', 'PUT', 'DELETE'])
def category(category_id):
    if request.method == 'GET':
        return category_resource.get(category_id)
    elif request.method == 'PUT':
        return category_resource.put(category_id)
    elif request.method == 'DELETE':
        return category_resource.delete(category_id)
