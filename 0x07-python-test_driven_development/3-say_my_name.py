#!/usr/bin/python3
"""Module containing function Say my name that prints a full name"""


def say_my_name(first_name, last_name=""):
    """A name introduction

Args:
    first_name (str): First name
    last_name (str): Last Name

Raises:
    TypeError: if either name is non string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
