#!/usr/bin/python3
"""Task 10 Module"""
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2], sys.argv[1])
    response = requests.get(
        url=url,
        data={
            "repo": sys.argv[1],
            "owner": sys.argv[2],
        },
    )
    data = response.json()
    print(data)
    for i in range(10):
        print(data[i].get("sha"), data[i].get("commit").get("author").get("name"))
