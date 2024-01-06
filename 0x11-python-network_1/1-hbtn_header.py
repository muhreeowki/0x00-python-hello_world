#!/usr/bin/python3
"""Task 1 Module"""
import urllib.request
import sys

url = sys.argv[1]
req = urllib.request.Request(url=url)
with urllib.request.urlopen(req) as response:
    print(response.headers["X-Request-Id"])
