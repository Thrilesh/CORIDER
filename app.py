from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask_restful import Resource, Api

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/user_management'
client = MongoClient(app.config['MONGO_URI'])
db = client.get_database()
users_collection = db.users

class User:
    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            'id': str(self.user_id),
            'name': self.name,
            'email': self.email,
            'password': self.password
        }

class AllUsersResource(Resource):
    def get(self):
        users = users_collection.find()
        user_list = [User(user['_id'], user['name'], user['email'], user['password']).to_dict() for user in users]
        return jsonify(user_list)

    def post(self):
        user_data = request.get_json()
        if 'name' in user_data and 'email' in user_data and 'password' in user_data:
            user = User(None, user_data['name'], user_data['email'], user_data['password'])
            result = users_collection.insert_one(user.__dict__)
            user.user_id = result.inserted_id
            return jsonify({'message': 'User created successfully', 'id': str(user.user_id)}), 201
        else:
            return jsonify({'error': 'Incomplete user data'}), 400

    def delete(self):
        users_collection.delete_many({})
        return jsonify({'message': 'All users deleted successfully'}), 200

class SingleUserResource(Resource):
    def get(self, user_id):
        user = users_collection.find_one({'_id': ObjectId(user_id)})
        if user:
            user_obj = User(user['_id'], user['name'], user['email'], user['password'])
            return jsonify(user_obj.to_dict())
        else:
            return jsonify({'error': 'User not found'}), 404

    def put(self, user_id):
        user_data = request.get_json()
        if 'name' in user_data or 'email' in user_data or 'password' in user_data:
            updated_fields = {key: value for key, value in user_data.items() if key in ['name', 'email', 'password']}
            result = users_collection.update_one({'_id': ObjectId(user_id)}, {'$set': updated_fields})
            if result.modified_count > 0:
                return jsonify({'message': 'User updated successfully'})
            else:
                return jsonify({'error': 'User not found'}), 404
        else:
            return jsonify({'error': 'No fields to update'}), 400

class DeleteSingleUserResource(Resource):
    def delete(self, user_id):
        result = users_collection.delete_one({'_id': ObjectId(user_id)})
        if result.deleted_count > 0:
            return jsonify({'message': 'User deleted successfully'})
        else:
            return jsonify({'error': 'User not found'}), 404

api = Api(app)
api.add_resource(AllUsersResource, '/users')
api.add_resource(SingleUserResource, '/users/<string:user_id>')
api.add_resource(DeleteSingleUserResource, '/users/<string:user_id>')  # New resource for individual user deletion

@app.route('/')
def hello():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
