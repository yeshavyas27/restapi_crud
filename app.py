from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

app = Flask(__name__)
client = MongoClient(MONGODB_HOST, MONGODB_PORT)
db = client["database"]
users_collection = db["users"]


@app.route('/add', methods=['POST'])
def add_user():
    name = request.args.get('name')
    email = request.args.get('email')
    password = request.args.get('pwd')
    # validate the received values
    if name and email and password and request.method == 'POST':
        #do not save password as a plain text
        hashed_password = generate_password_hash(password)
        # save details
        user = users_collection.insert_one({'name': name, 'email': email, 'pwd': hashed_password})
        resp = jsonify('User added successfully!')
        resp.status_code = 200
        return resp
    else:
        return not_found()


@app.route("/users", methods=['GET'])
def users_data():
    users = users_collection.find()
    response = dumps(users)
    return response


@app.route('/user/<id>', methods=["GET"])
def user(id):
    user = users_collection.find_one({'_id': ObjectId(id)})
    resp = dumps(user)
    return resp


@app.route('/update', methods=['PUT'])
def update_user():

    id = request.args.get('id')
    name = request.args.get('name')
    email = request.args.get('email')
    password = request.args.get('pwd')
    # validate the received values
    if name and email and password and id and request.method == 'PUT':
        # do not save password as a plain text
        hashed_password = generate_password_hash(password)
        # save edits
        users_collection.update_one({'_id': ObjectId(id['$oid']) if '$oid' in id else ObjectId(id)},
                                 {'$set': {'name': name, 'email': email, 'pwd': hashed_password}})
        resp = jsonify('User updated successfully!')
        resp.status_code = 200
        return resp
    else:
        return not_found()


@app.route('/delete/<id>', methods=['DELETE'])
def delete_user(id):
    users_collection.delete_one({'_id': ObjectId(id)})
    resp = jsonify('User deleted successfully!')
    resp.status_code = 200
    return resp


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


if __name__ == "__main__":
    app.run(debug=True)