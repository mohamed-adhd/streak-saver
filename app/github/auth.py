from http.cookiejar import request_port

import pygithub
from dotenv import load_dotenv
import os

def initiate():
    load_dotenv()
    token =os.getenv('TOKEN')
    repo = os.getenv('REPO')
    username = os.getenv('USER_NAME')
    if token is None:
        print("nigga put the damn token")
    if repo is None:
        print("nigga put the damn repo name")
    if username is None:
        print("nigga put the damn username")



