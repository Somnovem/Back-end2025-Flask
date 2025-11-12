from flask import request, jsonify
from flask import current_app as app
import uuid

users = {}


@app.post('/user')
def create_user():
    data = request.get_json()
    user_id = uuid.uuid4().hex
    user = {"id": user_id, "name": data.get("name")}
    users[user_id] = user
    return jsonify(user), 201


@app.get('/users')
def get_users():
    return jsonify(list(users.values())), 200


@app.get('/user/<user_id>')
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200


@app.delete('/user/<user_id>')
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return 'User successfully deleted', 204
    return jsonify({"error": "User not found"}), 404
