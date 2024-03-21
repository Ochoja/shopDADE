# Online Shopping Site(shopDADE) - Backend

This repository contains the backend code for an online shopping site project (shopDADE).

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The backend of the online shopping site is responsible for handling user authentication, product management, order processing, and interactions with the database. It provides RESTful API endpoints for the frontend to communicate with.

## Technologies Used

- Python Flask: Web framework for building the backend server.
- MongoDB: NoSQL database for storing product, user, order, and payment data.
- Flask-PyMongo: Flask extension for integrating MongoDB with Flask applications.
- Flask-RESTful: Flask extension for creating RESTful APIs.
- JWT (JSON Web Tokens): For user authentication and authorization.
- Other Python packages: Required packages are listed in the `requirements.txt` file.

## Setup Instructions

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/Ochoja/shopDADE/backend.git
   ```

2. Navigate to the project directory:
   ```bash
   cd backend
   ```

3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

6. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add the following environment variables to the `.env` file:
     ```
     FLASK_APP=app.py
     FLASK_ENV=development
     MONGO_URI=mongodb://localhost:27017/Capstone
     SECRET_KEY=<your_secret_key>
     ```

7. Run the Flask development server:
   ```bash
   flask run
   ```
    or

   ```bash
   python app.py
   ```

8. The backend server should now be running locally on http://localhost:5000.

## API Endpoints

The following API endpoints are available:

- `/api/auth/register`: POST method to register a new user.
- `/api/auth/login`: POST method to authenticate and log in a user.
- `/api/auth/logout`: POST method to log out a user.
- `/api/products`: GET method to retrieve all products.
- `/api/products/<product_id>`: GET, PUT, DELETE methods for a specific product.
- `/api/orders`: GET method to retrieve all orders.
- `/api/orders/<order_id>`: GET, PUT, DELETE methods for a specific order.
- `/api/users`: GET method to retrieve all users (admin access only).
- `/api/users/<user_id>`: GET, PUT, DELETE methods for a specific user (admin access only).

For detailed information on each endpoint and their request/response formats, refer to the API documentation.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

---
