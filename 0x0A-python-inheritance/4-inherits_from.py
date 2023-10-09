#!/usr/bin/python3
"""
Module that contains inherits_from function
"""


def inherits_from(obj, a_class):
    """
    Function that returns True if the object is an
    instance of a class that inherited (directly or indirectly)
    the specified class ; otherwise False
    """
    return issubclass(type(obj), a_class) if type(obj) is not a_class \
        else False
