#!/usr/bin/python3
"""Task 2 Module"""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = "" if len(sys.argv) < 2 else sys.argv[1]
    response = requests.post(url=url, data={"q": q})
    try:
        data = response.json()
        if data == {}:
            print("No result")
        else:
            print("[{}] {}".format(data.get("id"), data.get("name")))
    except Exception:
        print("Not a valid JSON")
