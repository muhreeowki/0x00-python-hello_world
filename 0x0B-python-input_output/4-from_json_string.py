#!/usr/bin/python3
"""Module containing from_json_string funtion"""
import json


def from_json_string(my_str):
    """Function that returns an object
    (Python data structure) represented by a JSON string"""
    return json.loads(my_str)
