from github import Github
from datetime import datetime
from . import auth

def clinet_on (token):
    g= auth.initiate(token)
    s=Github(auth=g)
    return s