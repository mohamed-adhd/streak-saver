#from . import commits
from . import client, commits


def mainy(token,repo,file,username):
    s=client.clinet_on(token)
    if (commits.fetch(s,username)=="save"):
        commits.commit(s,username,repo,file)
def checky(token,repo,file,username):
    s=client.clinet_on(token)
    if (commits.fetch(s,username)=="save"):
        return "fucked"

#streak-saver-bot on 2026-08-22

#streak-saver-bot on 2026-09-27

#streak-saver-bot on 2026-09-28

#streak-saver-bot on 2026-10-02

#streak-saver-bot on 2026-10-03

#streak-saver-bot on 2026-10-07

#streak-saver-bot on 2026-10-08

#streak-saver-bot on 2026-10-10

#streak-saver-bot on 2026-10-11

#streak-saver-bot on 2026-10-16

#streak-saver-bot on 2026-10-17

#streak-saver-bot on 2026-10-20

#streak-saver-bot on 2026-10-21

#streak-saver-bot on 2026-10-22

#streak-saver-bot on 2026-10-23

#streak-saver-bot on 2026-10-24

#streak-saver-bot on 2026-10-25

#streak-saver-bot on 2026-10-26

#streak-saver-bot on 2026-10-27
