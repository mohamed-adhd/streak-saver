import auth
import commits
import client

def main():
    s=client.clinet_on()
    if (commits.fetch(s,"mohamed-adhd")=="save"):
        commits.commit(s,"mohamed-adhd","streak-saver","app/github/__init__.py")

main()
