#!/usr/bin/python3
"""get 10 commits of a user"""


import requests
import sys


if __name__ == "__main__":
    user = sys.argv[2]
    repo = sys.argv[1]
    url = f"https://api.github.com/repos/{user}/{repo}/commits"
    res = requests.get(url)
    try:
        commits = res.json()
        for i in range(10):
            sha = commits[i].get('sha')
            author_name = commits[i].get("author").get("name")
            print(f"{sha}: {author_name}")
    except Exception as e:
        pass
