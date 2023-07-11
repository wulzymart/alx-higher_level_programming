#!/usr/bin/python3
"""Module containing student class"""


class Student:
    """class of students"""
    def __init__(self, first_name, last_name, age):
        """initializes a Student instance"""
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def to_json(self, attrs=None):
        """retrieves a list attributes with values
        from dictionary representation of the instance
        if list is not a list of strings, return all dicts
        """
        if isinstance(attrs, list) and\
                all(isinstance(ele, str) for ele in attrs):
            self_dict = self.__dict__
            attr_dict = {}
            for ele in attrs:
                if ele in self_dict:
                    attr_dict[ele] = self_dict[ele]
            return attr_dict
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance from json"""
        for key, value in json.items():
            setattr(self, key, value)
