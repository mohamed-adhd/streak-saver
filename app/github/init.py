from . import commits
from . import client

def mainy(token,repo,file,username):
    s=client.clinet_on(token)
    if (commits.fetch(s,username)=="save"):
        commits.commit(s,username,repo,file)

