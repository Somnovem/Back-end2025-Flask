from flask import Flask

app = Flask(__name__)

from myapp import views, users, categories, records  # noqa: E402


def seed_data():
    if not users.users:
        users.users.update({
            "u1": {"id": "u1", "name": "Alice"},
            "u2": {"id": "u2", "name": "Bob"},
        })

    if not categories.categories:
        categories.categories.update({
            "c1": {"id": "c1", "name": "Food"},
            "c2": {"id": "c2", "name": "Transport"},
        })

    if not records.records:
        from datetime import datetime
        records.records.update({
            "r1": {
                "id": "r1",
                "user_id": "u1",
                "category_id": "c1",
                "created_at": datetime.utcnow().isoformat() + "Z",
                "amount": 15.5
            },
            "r2": {
                "id": "r2",
                "user_id": "u2",
                "category_id": "c2",
                "created_at": datetime.utcnow().isoformat() + "Z",
                "amount": 7.0
            }
        })


seed_data()
