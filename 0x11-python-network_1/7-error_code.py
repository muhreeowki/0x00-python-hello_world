#!/usr/bin/python3
"""Task 3 Module"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        response = requests.get(url)
        print(response.content.decode())
    except requests.exceptions.HTTPError as error:
        print("Error code: {}".format(error))
