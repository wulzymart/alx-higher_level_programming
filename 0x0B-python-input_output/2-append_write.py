#!/usr/bin/python3
"""Module containing append write function"""


def append_write(filename="", text=""):
    """Appends a text to a given file"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
