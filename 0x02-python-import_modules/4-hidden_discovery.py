#!/usr/bin/python3
import hidden_4
for str in dir(hidden_4):
    if str[0] != "_":
        print("{}".format(str))
