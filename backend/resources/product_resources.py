from flask import jsonify, current_app
from flask_restful import Resource, reqparse
from models.product import Product
from werkzeug.utils import secure_filename
import os
from werkzeug.datastructures import FileStorage


class ProductListResource(Resource):
    def get(self):
        products = Product.find_all()
        serialized_products = [{'_id': str(product['_id']), 'title': product['title'], 'description': product['description'],
                                'price': product['price'], 'stock_quantity': product['stock_quantity'],
                                'category_id': product['category_id'], 'image_url': product['image_url']} for product in products if 'category_id' in product]
        return jsonify({'products': serialized_products})

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True)
        parser.add_argument('description', type=str)
        parser.add_argument('price', type=float, required=True)
        parser.add_argument('stock_quantity', type=int, default=0)
        parser.add_argument('category_id', type=str, required=True)
        parser.add_argument('image_file', type=FileStorage, location='files')  # New argument for file upload
        args = parser.parse_args()

        # Handle file upload
        image_filename = None
        if args['image_file']:
            try:
                image_filename = secure_filename(args['image_file'].filename)
                # Check file extension
                allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
                if not image_filename.lower().endswith(tuple(allowed_extensions)):
                    return {'message': 'Invalid image format. Only {} files are allowed.'.format(', '.join(allowed_extensions))}, 400

                upload_folder = current_app.config['UPLOAD_FOLDER']
                args['image_file'].save(os.path.join(upload_folder, image_filename))
            except Exception as e:
                return {'message': 'File upload not allowed'}, 400

        product = Product(title=args['title'], description=args['description'], price=args['price'],
                          stock_quantity=args['stock_quantity'], category_id=args['category_id'], image_url=image_filename)

        product.save()

        return {'_id': str(product._id), 'title': product.title, 'description': product.description,
                'price': product.price, 'stock_quantity': product.stock_quantity,
                'category_id': product.category_id, 'image_url': product.image_url}, 201


class ProductResource(Resource):
    def get(self, product_id):
        product = Product.find_by_id(product_id)
        return {'product': {'_id': str(product['_id']), 'title': product['title'], 'description': product['description'], 
                            'price': product['price'], 'stock_quantity': product['stock_quantity'], 
                            'category_id': product.get('category_id'), 'image_url': product.get('image_url')}}

    def put(self, product_id):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str)
        parser.add_argument('description', type=str)
        parser.add_argument('price', type=float)
        parser.add_argument('stock_quantity', type=int)
        parser.add_argument('category_id', type=str)
        parser.add_argument('image_file', type=str)  # Assuming you only update metadata, not the image itself
        args = parser.parse_args()

        update_data = {key: value for key, value in args.items() if value is not None}
        Product.update_by_id(product_id, update_data)
        return {'message': 'Product updated successfully'}, 200

    def delete(self, product_id):
        Product.delete_by_id(product_id)
        return {'message': 'Product deleted successfully'}, 200
