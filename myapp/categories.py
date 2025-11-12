from flask import request, jsonify
from myapp import app
import uuid

categories = {}


@app.post('/category')
def create_category():
    data = request.get_json()
    category_id = uuid.uuid4().hex
    category = {"id": category_id, "name": data.get("name")}
    categories[category_id] = category
    return jsonify(category), 201


@app.get('/category')
def get_categories():
    return jsonify(list(categories.values())), 200


@app.delete('/category')
def delete_category():
    data = request.get_json()
    category_id = data.get("id")
    if category_id in categories:
        del categories[category_id]
        return '', 204
    return jsonify({"error": "Category not found"}), 404
