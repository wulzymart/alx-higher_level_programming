#!/usr/bin/python3
"""Module containing append after function"""


def append_after(filename="", search_string="", new_string=""):
    """appends a string to a line after occurence of the string in the line

    Arguments:
    filename (string): name of file to search
    search_string (string): string to search for
    new_string (string): string to append
    """
    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()

    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
