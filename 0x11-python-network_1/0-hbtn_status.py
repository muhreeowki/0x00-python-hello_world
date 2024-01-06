#!/usr/bin/python3
"""Task 0 Module"""
if __name__ == "__main__":
    import urllib.request

    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print(
            "\t- type: {}\n\t- content: {}\n\t- utf8 content: {}".format(
                type(content), content, content.decode()
            )
        )
