#!/usr/bin/python3
"""Contains function to check if an object is a kind of a class"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of a class

    Arguments:
        obj: Object to check
        a_class: Class to check for

    Return: a boolean
    """

    return isinstance(obj, a_class)
