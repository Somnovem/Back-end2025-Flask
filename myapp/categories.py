from flask import request, jsonify
from flask import current_app as app
import uuid

categories = {}


@app.post('/category')
def create_category():
    data = request.get_json()
    category_id = uuid.uuid4().hex
    category = {"id": category_id, "name": data.get("name")}
    categories[category_id] = category
    return jsonify(category), 201


@app.get('/categories')
def get_categories():
    return jsonify(list(categories.values())), 200


@app.delete('/category')
def delete_category():
    data = request.get_json()
    category_id = data.get("id")
    if category_id in categories:
        del categories[category_id]
        return 'Category successfully deleted', 204
    return jsonify({"error": "Category not found"}), 404
