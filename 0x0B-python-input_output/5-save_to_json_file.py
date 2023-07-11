#!/usr/bin/python3
"""Module containing save to json file function"""


import json


def save_to_json_file(my_obj, filename):
    """Saves an object to a file as a json string"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
