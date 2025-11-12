from flask import Flask

from flask import Flask

app = Flask(__name__)
app.app_context().push()


def seed_data():
    from datetime import datetime

    inner_users_data = {
        "u1": {"id": "u1", "name": "Alice"},
        "u2": {"id": "u2", "name": "Bob"},
    }

    inner_categories_data = {
        "c1": {"id": "c1", "name": "Food"},
        "c2": {"id": "c2", "name": "Transport"},
    }

    inner_records_data = {
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
    }

    return inner_users_data, inner_categories_data, inner_records_data


users_data, categories_data, records_data = seed_data()

from myapp import users, categories, records, views  # noqa: E402

users.users.update(users_data)
categories.categories.update(categories_data)
records.records.update(records_data)
