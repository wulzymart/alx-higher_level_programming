#!/usr/bin/python3
"""Module containing function that adds an atribute to an object"""


def add_attribute(obj: object, name: str, value: any):
    """adds an attribute with a value to an object
    Arguments:
        obj: Object to get a new attribute
        name (string): name of vavue to add
        value (any): value to be added
    Raises:
        TypeError: if attribute can not be added to the object
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
