#!/usr/bin/python3
"""Module containing Student class"""


class Student:
    """Class that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Constructor method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method that retrieves a dictionary representation
        of a Student instance"""
        if isinstance(attrs, list) and len(attrs) > 0:
            attrs_to_return = {}
            for attr in attrs:
                if attr in self.__dict__:
                    attrs_to_return[attr] = self.__dict__[attr]
            return attrs_to_return

        else:
            return self.__dict__
