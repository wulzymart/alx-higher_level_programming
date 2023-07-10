#!/usr/bin/python3
"""Module of Class containing rebel integer"""


class MyInt(int):
    """Class containing a rebel int"""

    def __eq__(self, other):
        """reverses equality
        other: other value being compared with
        """

        return self.real != other

    def __ne__(self, other):
        """reverses inequality
        other: other value being compared with
        """
        return self.real == other
