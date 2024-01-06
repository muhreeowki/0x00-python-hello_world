#!/usr/bin/python3
"""Task 1 Module"""
import urllib.request
import sys

url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    print(response.headers["X-Request-Id"])
