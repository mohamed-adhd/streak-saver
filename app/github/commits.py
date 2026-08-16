
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
    new_shi = content_file.decoded_content.decode("utf-8") + ("\nstreak-saver-bot on " + today + "\n")
    rep.update_file(path=file,message="streak-saver got u ;)",content=new_shi,sha=content_file.sha)