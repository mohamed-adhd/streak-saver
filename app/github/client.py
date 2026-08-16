from github import Github
from datetime import datetime
import auth

def clinet_on ():
    g= auth.initiate()
    s=Github(auth=g)
    return s