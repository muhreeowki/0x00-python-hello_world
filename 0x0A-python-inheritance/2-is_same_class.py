"""
Module that contains is_same_class function
that checks if an object is in a specified class
"""


def is_same_class(obj, a_class):
    """
    Function that returns True if the object is exactly an instance
    of the specified class; otherwise False
    """
    return True if type(obj) is a_class else False
