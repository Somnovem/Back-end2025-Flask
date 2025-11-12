from datetime import datetime
from flask import request, jsonify
from myapp import app
from myapp.users import users
from myapp.categories import categories
import uuid

records = {}


@app.post('/record')
def create_record():
    data = request.get_json()
    user_id = data.get("user_id")
    category_id = data.get("category_id")
    amount = data.get("amount")

    if user_id not in users:
        return jsonify({"error": "Invalid user_id"}), 400
    if category_id not in categories:
        return jsonify({"error": "Invalid category_id"}), 400

    record_id = uuid.uuid4().hex
    record = {
        "id": record_id,
        "user_id": user_id,
        "category_id": category_id,
        "created_at": datetime.utcnow().isoformat() + "Z",
        "amount": amount
    }
    records[record_id] = record
    return jsonify(record), 201


@app.get('/record/<record_id>')
def get_record(record_id):
    record = records.get(record_id)
    if not record:
        return jsonify({"error": "Record not found"}), 404
    return jsonify(record), 200


@app.delete('/record/<record_id>')
def delete_record(record_id):
    if record_id in records:
        del records[record_id]
        return 'Record successfully deleted', 204
    return jsonify({"error": "Record not found"}), 404


@app.get('/record')
def get_records():
    user_id = request.args.get("user_id")
    category_id = request.args.get("category_id")

    if not user_id and not category_id:
        return jsonify({"error": "Provide user_id and category_id"}), 400

    result = [
        r for r in records.values()
        if (not user_id or r["user_id"] == user_id) and
           (not category_id or r["category_id"] == category_id)
    ]
    return jsonify(result), 200
