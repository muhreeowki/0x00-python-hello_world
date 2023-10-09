#!/usr/bin/python3
"""
Module that contains is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """
    Function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherits
    the specified class ; otherwise False
    """
    return True if isinstance(obj, a_class) else False
