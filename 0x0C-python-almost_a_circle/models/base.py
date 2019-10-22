#!/usr/bin/python3
"""Base Module"""
from json import dumps, loads


class Base:
    """Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Dictionary to Json string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return dumps([])
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON string to file"""
        list_o = []
        name = cls.__name__
        nameC = "{}{}".format(name, ".json")
        if list_objs:
            for objects in list_objs:
                list_o.append(objects.to_dictionary())
        with open(nameC, 'w', encoding='utf-8') as json_file:
            json_file.write(cls.to_json_string(list_o))
