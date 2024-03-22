import base64

with open('./static/uploads/image.png', 'rb') as image_file:
    encoded_image = base64.b64encode(image_file.read())

print(encoded_image.decode('utf-8'))
