#!/usr/bin/python3
"""Task 2 Module"""
import urllib.request
import urllib.parse


if __name__ == "__main__":
    import urllib.request
    import sys

    data = urllib.parse.urlencode({"email": sys.argv[2]}).encode("ascii")
    req = urllib.request.Request(url=sys.argv[1], data=data)
    with urllib.request.urlopen(req) as response:
        print(response.decode())
