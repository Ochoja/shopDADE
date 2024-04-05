from flask import jsonify
from flask_restful import Resource, reqparse
from models.product import Product
from schemas import ProductSchema

product_schema = ProductSchema()

class ProductListResource(Resource):
    def get(self):
        products = Product.find_all()
        serialized_products = [product_schema.dump(product) for product in products]
        return jsonify({'products': serialized_products})

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('description', type=str)
        parser.add_argument('price', type=float, required=True)
        parser.add_argument('old_price', type=float)
        parser.add_argument('stock_quantity', type=int, default=0)
        parser.add_argument('category_id', type=str, required=True)
        parser.add_argument('image_url', type=str)
        args = parser.parse_args()

        existing_product = Product.find_by_name(args['name'])
        if existing_product:
            return {'message': 'Product with the same name already exists'}, 400

        product = Product(name=args['name'], description=args['description'], price=args['price'],
                          old_price=args.get('old_price'),
                          stock_quantity=args['stock_quantity'], category_id=args['category_id'], image_url=args['image_url'])

        product.save()

        serialized_product = product_schema.dump(product)
        return serialized_product, 201

class ProductResource(Resource):
    def get(self, product_id):
        product = Product.find_by_id(product_id)
        serialized_product = product_schema.dump(product)
        return serialized_product

    def put(self, product_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('description', type=str)
        parser.add_argument('price', type=float)
        parser.add_argument('old_price', type=float)
        parser.add_argument('stock_quantity', type=int)
        parser.add_argument('category_id', type=str)
        parser.add_argument('image_url', type=str)
        args = parser.parse_args()

        update_data = {key: value for key, value in args.items() if value is not None}
        Product.update_by_id(product_id, update_data)
        return {'message': 'Product updated successfully'}, 200

    def delete(self, product_id):
        Product.delete_by_id(product_id)
        return {'message': 'Product deleted successfully'}, 200
