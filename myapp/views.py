from datetime import datetime, timezone
from myapp import app

@app.route("/healthcheck")
def healthcheck():
    return {
        "status": "ok",
        "date": datetime.now(timezone.utc).isoformat()
    }, 200
