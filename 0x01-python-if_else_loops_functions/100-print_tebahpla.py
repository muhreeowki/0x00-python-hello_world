#!/usr/bin/python3
for i in range(25, -1, -1):
    print("{}".format(chr(i + 97) if i % 2 == 1 else chr(i + 65)), end="")
