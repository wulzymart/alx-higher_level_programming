#!/usr/bin/python3
"""module containing load from jason file function"""


import json


def load_from_json_file(filename):
    """Loads a json object from a file"""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)
