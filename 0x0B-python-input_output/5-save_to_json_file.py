#!/usr/bin/python3
"""Module containing from_json_string funtion"""
import json


def save_to_json_file(my_obj, filename):
    """unction that writes an Object to a text file,
    using a JSON representation"""
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
