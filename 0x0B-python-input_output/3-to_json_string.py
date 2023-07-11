#!/usr/bin/python3
"""Module containing the to_json_string function"""

import json


def to_json_string(my_obj):
    """converts any object to jsdon string"""
    return json.dumps(my_obj)
