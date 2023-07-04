#!/usr/bin/python3
"""Module containing class lockedclass"""


class LockedClass:
    """Empty class that cannot have new attribute set except first_name"""
    __slots__ = ["first_name"]
