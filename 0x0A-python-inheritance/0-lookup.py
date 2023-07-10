#!/usr/bin/python3
"""Module containing lookup function"""


def lookup(obj):
    """returns a list containg all attributes and methods of an object"""
    return dir(obj)
