#!/usr/bin/python3
"""Contains function to check if an object inherits from a class"""


def inherits_from(obj, a_class):
    """Checks if an object inherits from a class

    Arguments:
        obj: Object to check
        a_class: Class to check for

    Return: a boolean
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
