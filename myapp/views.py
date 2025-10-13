from myapp import app

@app.route("/healthcheck")
def healthcheck():
    return {"status": "ok"}, 200
