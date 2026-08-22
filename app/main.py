from fastapi import FastAPI
import app
from upstash_redis import redis
import os
from cryptography.fernet import Fernet
from pydantic import BaseModel
class SetupRequest(BaseModel):
    username: str
    repo: str
    file: str
    token: str
app = FastAPI()
@app.post("/status")
def status():
    return {"status": "ok"}

@app.post("/setup")
def setup(data: SetupRequest):
    os.environ['TOKEN'] = data.token
    os.environ['REPO'] = data.repo
    os.environ['FILE'] = data.file
    os.environ['USERNAME'] = data.username

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