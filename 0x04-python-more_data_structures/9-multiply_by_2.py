#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if not a_dictionary:
        return {}
    return {a: a_dictionary[a] * 2 for a in a_dictionary.keys()}
