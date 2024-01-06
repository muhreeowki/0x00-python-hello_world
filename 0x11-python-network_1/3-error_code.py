#!/usr/bin/python3
"""Task 3 Module"""
import urllib.parse
import urllib.error
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode())
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
