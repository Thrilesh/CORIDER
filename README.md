# CORIDER
# Flask-RESTful User Management API

The Flask-RESTful User Management API is a simple web application that provides RESTful endpoints for managing user data.

## Requirements

- Python (3.6+)
- Flask
- Flask-RESTful
- pymongo

## Installation

1. Clone the repository:
git clone 'https://github.com/Thrilesh/CORIDER.git'
cd CORIDER
1.Install the required dependencies:
pip install -r requirements.txt

**Configuration**
Make sure you have MongoDB running on localhost:27017 or update the MONGO_URI in app.py to match your MongoDB server configuration.

**Usage**
Start the Flask app by running: python app.py
The API will run at http://127.0.0.1:5000.

**Endpoints**
GET /users: Get a list of all users.
GET /users/<user_id>: Get a specific user by their ID.
POST /users: Create a new user. (Request Body: {"name": "user_name", "email": "user_email", "password": "user_password"})
PUT /users/<user_id>: Update an existing user. (Request Body: {"name": "updated_name", "email": "updated_email", "password": "updated_password"})
DELETE /users: Delete all users.
DELETE /users/<user_id>: Delete a specific user by their ID.

**License**
This project is licensed under the MIT License - see the LICENSE file for details.




