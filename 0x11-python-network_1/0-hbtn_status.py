#!/usr/bin/python3
"""Task 0 Module"""
import urllib.request


with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    content = response.read()
    print(
        "Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}".format(
            type(content), content, content.decode()
        )
    )
