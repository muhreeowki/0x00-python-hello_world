#!/usr/bin/python3
"""
    This module contains the 'say_my_name' function from task 2
"""

def say_my_name(first_name, last_name=""):
    """ 
    Function that prints My name is <first name> <last name>

    Args:
        first_name: first name of user
        last_name: last name of user (optional)

    Returns:
        Nothing

    Raises:
        TypeError: If first_name or last_name is not a string

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
