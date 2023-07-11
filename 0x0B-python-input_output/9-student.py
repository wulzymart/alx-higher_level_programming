#!/usr/bin/python3
"""Module containing student class"""


class Student:
    """class of students"""
    def __init__(self, first_name, last_name, age):
        """initializes a Student instance"""
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def to_json(self):
        """retrieves a dictionary representation of the instance"""
        return self.__dict__
