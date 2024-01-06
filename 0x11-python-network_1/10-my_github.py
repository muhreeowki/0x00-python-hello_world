#!/usr/bin/python3
"""Task 2 Module"""
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/user"
    response = requests.get(
        url=url,
        data={"username": sys.argv[1]},
        headers={"Authorization": "Bearer {}".format(sys.argv[2])},
    )
    try:
        data = response.json()
        if data == {}:
            print("None")
        else:
            print(data.get("id"))
    except Exception:
        ...
