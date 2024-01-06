#!/usr/bin/python3
"""Task 4 Module"""
import requests

if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    content = response.content.decode()
    print("Body response:")
    print("\t- type: {}\n\t- content: {}".format(type(content), content))
