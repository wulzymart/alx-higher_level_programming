#!/usr/bin/python3
"""takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user
with the letter as a parameter."""

import requests
import sys


if __name__ == "__main__":
    data = {"q": sys.argv[1] if len(sys.argv) > 1 else ""}
    res = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        jsonRes = res.json()
        if jsonRes:
            print(f"[{jsonRes.get('id')}] {jsonRes.get('name')}")
        else:
            print("No result")
    except Exception as e:
        print("Not a valid JSON")
