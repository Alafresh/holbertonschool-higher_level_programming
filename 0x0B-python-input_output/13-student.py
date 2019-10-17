#!/usr/bin/python3


class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dict_2 = {}
        if attrs is None:
            return self.__dict__
        for i in attrs:
            if i in self.__dict__.keys():
                dict_2[i] = self.__dict__[i]
        return dict_2

    def reload_from_json(self, json):
        if json == {}:
            pass
        else:
            self.first_name = json["first_name"]
            self.last_name = json["last_name"]
            self.age = json["age"]
