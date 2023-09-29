#!/usr/bin/python3
"""takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""


import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    access_token = sys.argv[2]
    headers = {"Accept": "application/vnd.github+json",
               "Authorization": f"Bearer {access_token}",
               "X-GitHub-Api-Version": "2022-11-28"
               }
    res = requests.get(f"https://api.github.com/users/{user}",
                       headers=headers)
    print(res.json().get("id"))
