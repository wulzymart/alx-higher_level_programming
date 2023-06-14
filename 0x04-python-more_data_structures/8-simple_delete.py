#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if not key or not a_dictionary:
        return a_dictionary if a_dictionary else {}
    if key in a_dictionary:
        del (a_dictionary[key])
    return a_dictionary
