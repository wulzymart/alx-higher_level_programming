#!/usr/bin/python3
"""Module containing write file function
"""


def write_file(filename="", text=""):
    """Writes a string to a file using utf-8 encoding"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
