import sys
from dotenv import load_dotenv
import os
from github import Auth
def initiate():
    load_dotenv()
    token =os.getenv('TOKEN')
    repo = os.getenv('REPO')
    username = os.getenv('USER_NAME')
    if token is None:
        print("nigga put the damn token")
        sys.exit(1)
    auth = Auth.Token(token)
    return auth



