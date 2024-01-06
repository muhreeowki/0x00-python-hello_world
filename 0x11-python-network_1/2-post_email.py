#!/usr/bin/python3
"""Task 2 Module"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    data = urllib.parse.urlencode({"email": sys.argv[2]})
    data = data.encode("ascii")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode())
