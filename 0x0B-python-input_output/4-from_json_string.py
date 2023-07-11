#!/usr/bin/python3
"""Module containing from_Json function"""


import json


def from_json_string(my_str):
    """converts a JSON string to an object"""
    return json.loads(my_str)
