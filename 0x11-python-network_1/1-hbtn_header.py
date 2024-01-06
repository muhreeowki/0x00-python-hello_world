#!/usr/bin/python3
"""Task 1 Module"""
if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers.get("X-Request-Id"))
