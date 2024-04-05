from marshmallow import Schema, fields


class ProductSchema(Schema):
    _id = fields.Str(required=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    price = fields.Float(required=True)
    old_price = fields.Float(required=True)
    stock_quantity = fields.Int(required=True)
    category = fields.Str(required=True)
    image_url = fields.List(fields.Str(), required=True)  # List of image URLs
    sizes = fields.List(fields.Str())  # List of sizes


class OrderItemSchema(Schema):
    product = fields.Nested(ProductSchema, required=True)
    quantity = fields.Int(required=True)
    price = fields.Float(required=True)


class OrderSchema(Schema):
    _id = fields.Str(required=True)
    user = fields.Str(allow_none=True)
    items = fields.List(fields.Nested(OrderItemSchema), required=True)
    total_price = fields.Float(required=True)
    status = fields.Str(required=True)
    shipping_address = fields.Str()
    payment_details = fields.Str()
