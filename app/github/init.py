#from . import commits
from . import client, commits


def mainy(token,repo,file,username):
    s=client.clinet_on(token)
    if (commits.fetch(s,username)=="save"):
        commits.commit(s,username,repo,file)
def checky(username):
    s=client.clinet_on(token)
    if (commits.fetch(s,username)=="save"):
        return "fucked"

#streak-saver-bot on 2026-08-22
