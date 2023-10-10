#!/usr/bin/python3
"""
This is a script that adds all arguments to a
Python list and then save them to a file
"""

import json
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

items_list = []

if len(sys.argv) >= 2:
    for i in range(1, len(sys.argv)):
        items_list.append(sys.argv[i])

try:
    old = load_from_json_file("add_item.json")
    for item in old:
        items_list.append(item)
except FileNotFoundError:
    pass

save_to_json_file(items_list, "add_item.json")
