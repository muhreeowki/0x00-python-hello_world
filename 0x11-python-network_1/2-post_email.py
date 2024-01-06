#!/usr/bin/python3
"""Task 2 Module"""
import urllib.request
import urllib.parse


if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]
    data = urllib.parse.urlencode({"email": sys.argv[2]})
    data = data.encode("ascii")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.decode())
