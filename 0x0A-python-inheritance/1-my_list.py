#!/usr/bin/python3
"""Module for class MyList"""


class MyList(list):
    """A subclass of list"""

    def print_sorted(self):
        """prints sorted list in ascending order
        MyList must be list of integers
        """
        print(sorted(self))
