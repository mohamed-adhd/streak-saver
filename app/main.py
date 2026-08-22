from fastapi import FastAPI
import app
from upstash_redis import Redis
import os
from cryptography.fernet import Fernet
from pydantic import BaseModel


redis = Redis(
    url=os.environ["UPSTASH_REDIS_REST_URL"],
    token=os.environ["UPSTASH_REDIS_REST_TOKEN"],
)
fernet = Fernet(os.environ["ENCRYPTION_KEY"].encode())
CONFIG_KEY = "github_config"










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
import json

@app.post("/setup")
def setup(data: SetupRequest):
    encrypted_token = fernet.encrypt(data.token.encode()).decode()
    payload = {
        "token": encrypted_token,
        "repo": data.repo,
        "file": data.file,
        "username": data.username,
    }
    redis.set(CONFIG_KEY, json.dumps(payload))

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


def get_config():
    raw = redis.get(CONFIG_KEY)
    if not raw:
        return None
    payload = json.loads(raw)
    payload["token"] = fernet.decrypt(payload["token"].encode()).decode()
    return payload