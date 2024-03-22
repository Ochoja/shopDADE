from flask import jsonify, current_app
from flask_restful import Resource, reqparse
from models.product import Product
from schemas import ProductSchema
from werkzeug.utils import secure_filename
import os
import base64
from werkzeug.datastructures import FileStorage

# Instantiate the product schema
product_schema = ProductSchema()

# Helper function to encode image to base64
def encode_image_to_base64(image_path):
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
        base64_encoded = base64.b64encode(image_data)
        base64_image_string = base64_encoded.decode('utf-8')  # Convert bytes to string
        return base64_image_string

class ProductListResource(Resource):
    def get(self):
        products = Product.find_all()
        serialized_products = [product_schema.dump(product) for product in products]
        return jsonify({'products': serialized_products})

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('price', type=float, required=True)
        parser.add_argument('old_price', type=float)
        parser.add_argument('description', type=str)
        parser.add_argument('category', type=str)
        parser.add_argument('image_file', type=FileStorage, location='files')  # New argument for file upload
        parser.add_argument('sizes', type=list)  # Assuming sizes will be a list
        args = parser.parse_args()

        # Handle file upload and image encoding
        image_filename = None
        base64_image = None
        if args['image_file']:
            try:
                image_filename = secure_filename(args['image_file'].filename)
                # Save the image file
                upload_folder = current_app.config['UPLOAD_FOLDER']
                image_path = os.path.join(upload_folder, image_filename)
                args['image_file'].save(image_path)
                # Encode the image to base64
                base64_image = encode_image_to_base64(image_path)
            except Exception as e:
                return {'message': 'File upload or encoding error'}, 400

        product = Product(name=args['name'], price=args['price'], old_price=args['old_price'],
                          description=args['description'], category=args['category'], image_url=image_filename,
                          sizes=args['sizes'], image_base64=base64_image)

        product.save()

        return product_schema.dump(product), 201

class ProductResource(Resource):
    def get(self, product_id):
        product = Product.find_by_id(product_id)
        if product:
            return product_schema.dump(product)
        else:
            return {'message': 'Product not found'}, 404

    def put(self, product_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('price', type=float)
        parser.add_argument('old_price', type=float)
        parser.add_argument('description', type=str)
        parser.add_argument('category', type=str)
        parser.add_argument('image_file', type=str)  # Assuming you only update metadata, not the image itself
        parser.add_argument('sizes', type=list)  # Assuming sizes will be a list
        args = parser.parse_args()

        update_data = {key: value for key, value in args.items() if value is not None}
        Product.update_by_id(product_id, update_data)
        return {'message': 'Product updated successfully'}, 200

    def delete(self, product_id):
        Product.delete_by_id(product_id)
        return {'message': 'Product deleted successfully'}, 200
