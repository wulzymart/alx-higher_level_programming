#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        items = list(a_dictionary.items())
        for key, val in items:
            if val == value:
                del (a_dictionary[key])
    return a_dictionary
