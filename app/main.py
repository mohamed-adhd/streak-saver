from fastapi import FastAPI
import app
from pydantic import BaseModel
class SetupRequest(BaseModel):
    username: str
    repo: str
    file: str
    token: str
app = FastAPI()
@app.get("/status")
def status():
    return {"status": "ok"}

@app.post("/setup")
def setup(data: SetupRequest):
    return {
        "username": data.username,
        "repo": data.repo
    }
@app.get("/save")
def save():
    return {"status": "saved"}

@app.get("/")
def root():
    return {"message": "Streak-Saver API"}