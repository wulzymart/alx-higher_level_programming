#!/usr/bin/python3
"""modile containing readfile function"""


def read_file(filename=""):
    """Reads a file using the utf8 encoder"""
    with open(filename, encoding='utf-8') as file:
        print(file.read())
