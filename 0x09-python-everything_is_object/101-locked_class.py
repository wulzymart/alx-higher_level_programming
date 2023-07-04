#!/usr/bin/python3
"""Module containing class lockedclass"""


class LockedClass(object):
    """Empty class that cannot have new attribute set except first_name"""
    def __setattr__(self, key, value):
        if key != "first_name":
            raise AttributeError(f"'LockedClass' object has no attribute\
 '{key}'")
        object.__setattr__(self, key, value)
