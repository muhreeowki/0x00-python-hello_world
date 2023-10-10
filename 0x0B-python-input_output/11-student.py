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
        if attrs is not None and isinstance(attrs, list):
            attrs_to_return = {}
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
                if attr in self.__dict__:
                    attrs_to_return[attr] = self.__dict__[attr]
            return attrs_to_return

        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Method that replaces all attributes of the Student instance"""
        for attr in json:
            if attr in self.__dict__.keys():
                self.__dict__[attr] = json[attr]
