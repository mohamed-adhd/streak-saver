
from datetime import datetime
def fetch(s,username):
    today = datetime.now().strftime("%Y-%m-%d")
    commits = s.search_commits(query="author:" + username + " committer-date:"+today)
    if commits.totalCount != 0:
        return "safe"
    else:
        return "save"

def commit(s, username, repo, file):
    today = datetime.now().strftime("%Y-%m-%d")
    rep = s.get_repo(username + "/" + repo)
    content_file = rep.get_contents(file)
