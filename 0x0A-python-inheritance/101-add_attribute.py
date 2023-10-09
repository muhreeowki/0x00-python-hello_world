#!/usr/bin/python3
"""Module containing add_attribute function"""


def add_attribute(obj, name, value):
    """Function that adds a new attribute to an object if it’s possible"""
    try:
        obj.name = value
    except Exception:
        raise TypeError("can't add new attribute")
