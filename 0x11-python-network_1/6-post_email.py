#!/usr/bin/python3
"""Task 2 Module"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.post(url=url, data={"email": sys.argv[2]})
    print(response.content.decode())
