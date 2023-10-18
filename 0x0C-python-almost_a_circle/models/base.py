#!/usr/bin/python3
"""Module containing base class"""
import csv
import json


class Base:
    """This is the base class for all other classes in this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor method"""
        if id is None:
            Base.__nb_objects += 1
        self.id = id if id else Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return json.dumps([])
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves a json representation of a list of objects to a file"""
        obj_strings = []
        for obj in list_objs:
            obj_strings.append(obj.to_dictionary())
        with open("{}.json".format(cls.__name__), "w") as f:
            f.write(cls.to_json_string(obj_strings))
        
    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        json_list = []
        if json_string is not None and json_string != "":
            json_list = json.loads(json_string)
        return json_list

    @classmethod
    def create(cls, **dictionary):
        """
        Creates a new instance from the class 'cls' and instanciates
        it with the attributes in 'dictionary'
        """
        instance = cls(10, 10)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances that were stored
        in a json file
        """
        instance_list = []
        try:
            with open("{}.json".format(cls.__name__), 'r') as f:
                dictionary_list = cls.from_json_string(f.read())
                for d in dictionary_list:
                    instance_list.append(cls.create(**d))
        except FileNotFoundError:
            pass
        return instance_list


    @classmethod
    def load_from_file_csv(cls):
        """
        Returns a list of instances that were stored
        in a json file
        """
        instance_list = []
        try:
            with open("{}.csv".format(cls.__name__), 'r') as f:
                reader = csv.DictReader(f)
        except FileNotFoundError:
            pass
        return instance_list
