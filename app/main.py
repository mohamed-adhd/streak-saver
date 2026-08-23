from fastapi import FastAPI
from upstash_redis import Redis
import os
import HTMLResponse
import json
from cryptography.fernet import Fernet
from pydantic import BaseModel
import github
from app.streak import checker
from app.github import init
from app.github.commits import fetch
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
        "message": "done bitch"
    }
from fastapi.responses import HTMLResponse

@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <html>
      <head>
        <title>streak-saver</title>
        <style>
          body {
            margin: 0;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            background: radial-gradient(circle at 50% 30%, #1b1b26, #0d0d12);
            font-family: 'Segoe UI', Arial, sans-serif;
          }
          .card {
            text-align: center;
            padding: 40px;
          }
          h1 {
            color: white;
            font-size: 42px;
            margin-bottom: 8px;
            text-shadow: 0 0 30px rgba(91, 76, 255, 0.4);
          }
          .accent {
            width: 56px;
            height: 4px;
            margin: 12px auto 20px;
            border-radius: 2px;
            background: linear-gradient(90deg, #5B4CFF, #8F6BFF);
          }
          p {
            color: #9c9cac;
            font-size: 16px;
          }
          .status {
            display: inline-block;
            margin-top: 24px;
            padding: 8px 16px;
            border-radius: 20px;
            background: #1b1b24;
            border: 1px solid #2c2c38;
            color: #b9afff;
            font-size: 13px;
            letter-spacing: 1px;
          }
        </style>
      </head>
      <body>
        <div class="card">
          <h1>streak-saver</h1>
          <div class="accent"></div>
          <p>your github streak is being watched, relax twin</p>
          <div class="status">online dawg</div>
        </div>
      </body>
    </html>
    """



@app.get("/status")
def status():
    config = get_config()
    if not config:
        return {"error": "no config stored yet, call /setup first"}
    return {
        "token": "fuh naw" ,
        "repo": config["repo"] ,
        "file": config["file"] ,
        "username": config["username"]
    }

@app.get("/api/cron")
def cron():
    config = get_config()
    if not config:
        return {"error": "no config stored yet, call /setup first"}
    init.mainy(config["token"], config["repo"], config["file"], config["username"])
    return {"success": True}


# hmm , so i plan on checking from 22 till 23, i ll make 6 checks then
@app.get("/check1")
def check1():
    config = get_config()
    if init.checky(config["token"], config["repo"], config["file"], config["username"])=="fucked":
        checker.alert(1)
        return {"message": "alerted 1"}
    else :
        return {"message": "safe"}

@app.get("/check2")
def check2():
    config = get_config()

    if init.checky(config["token"], config["repo"], config["file"], config["username"]) == "fucked":
        checker.alert(2)
        return {"message": "alerted 2"}
    else :
        return {"message": "safe"}

@app.get("/check3")
def check3():
    config = get_config()

    if init.checky(config["token"], config["repo"], config["file"], config["username"]) == "fucked":
        checker.alert(3)
        return {"message": "alerted 3"}
    else :
        return {"message": "safe"}





def get_config():
    raw = redis.get(CONFIG_KEY)
    if not raw:
        return None
    payload = json.loads(raw)
    payload["token"] = fernet.decrypt(payload["token"].encode()).decode()
    return payload