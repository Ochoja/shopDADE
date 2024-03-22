from flask_restful import Resource, reqparse
from flask import request
from models.category import Category

class CategoryListResource(Resource):
    def get(self):
        categories = Category.find_all()
        return {'categories': categories}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('description', type=str)
        args = parser.parse_args()

        category = Category(**args)
        try:
            category.save()
            return {'id': str(category._id)}, 201
        except ValueError as e:
            return {'message': str(e)}, 400


class CategoryResource(Resource):
    def get(self, category_id):
        category = Category.find_by_id(category_id)
        return {'category': category}

    def put(self, category_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('description', type=str)
        args = parser.parse_args()

        # Check if both 'name' and 'description' are provided
        if 'name' not in args or 'description' not in args:
            return {'message': 'Both name and description are required'}, 400

        # Check if the new name is the same as the existing name
        existing_category = Category.find_by_name(args['name'])
        if existing_category and str(existing_category['_id']) != category_id:
            return {'message': 'Category with this name already exists'}, 409

        # Instantiate Category with name
        category = Category(args['name'])
        category.update_by_id(category_id, args['name'], args['description'])
        return {'message': 'Category updated successfully'}, 200

    def delete(self, category_id):
        Category.delete_by_id(category_id)
        return {'message': 'Category deleted successfully'}, 200
