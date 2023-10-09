#!/usr/bin/python3
"""Module containing add_attribute function"""


def add_attribute(obj, name, value):
    """Function that adds a new attribute to an object if it’s possible"""
    if '__slots__' in dir(obj) or '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
