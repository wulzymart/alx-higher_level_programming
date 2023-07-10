#!/usr/bin/python3
"""Module for class MyList"""


class MyList(list):
    """A subclass of list"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints sorted list in ascending order
        MyList must be list of integers
        """
        print(sorted(self))
