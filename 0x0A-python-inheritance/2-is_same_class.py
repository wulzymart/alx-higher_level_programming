#!/usr/bin/python3
"""Module containing is_same_class function"""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of a class

    Arguments:
        obj: Object to check
        a_class: Class to check for

    Return: a boolean
    """
    return type(obj) == a_class
