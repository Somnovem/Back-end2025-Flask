from datetime import datetime, timezone
from flask import current_app as app


@app.route("/healthcheck")
def healthcheck():
    return {
        "status": "ok",
        "date": datetime.now(timezone.utc).isoformat()
    }, 200
