from github import Github

import auth

def clinet_on ():
    g= auth.initiate()
    s=Github(auth=g)
    print(s.search_repositories(query="language:python"))


clinet_on()