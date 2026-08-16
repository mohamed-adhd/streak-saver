from datetime import datetime
def fetch(s,username):
    today = datetime.now().strftime("%Y-%m-%d")
    commits = s.search_commits(query="author:" + username + " committer-date:2026-08-15")
    if commits is not None:
        return "safe"
    else:
        return "save"

def commit(s,username,repo,file):
    today = datetime.now().strftime("%Y-%m-%d")
    rep = s.get_repo("mohamed-adhd/"+repo)
    file = repo.get_contents(file)
    

