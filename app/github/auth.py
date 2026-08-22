import sys
from dotenv import load_dotenv
import os
from github import Auth
def initiate(token):
    auth = Auth.Token(token)
    return auth



