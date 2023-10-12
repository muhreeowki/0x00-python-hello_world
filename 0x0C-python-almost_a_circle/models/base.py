#!/usr/bin/python3
"""Module containing base class"""

class Base:
    """This is the base class for all other classes in this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor method"""
        Base.__nb_objects += 1
        self.id = id if id is not None else Base.__nb_objects
