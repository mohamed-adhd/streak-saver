from github import Github
from datetime import datetime
import auth

def clinet_on (username):
    g= auth.initiate()
    s=Github(auth=g)
    today = datetime.now().strftime("%Y-%m-%d")
    commits=s.search_commits(query="author:"+username+" committer-date:2026-08-15")
    for commit in commits:
        print(commit)


clinet_on("mohamed-adhd")