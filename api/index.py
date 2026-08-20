import app


@app.get("/status")
def status():
    return {"status": "ok"}

@app.get("/setup")
def setup():
    return {"status": "sucess"}

@app.get("/save")
def save():
    return {"status": "saved"}

@app.get("/")
def root():
    return {"message": "Streak-Saver API"}