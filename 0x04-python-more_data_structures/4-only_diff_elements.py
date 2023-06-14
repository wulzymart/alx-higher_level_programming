#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if not set_1 or not set_2:
        return set_1 if set_1 else set_2
    return set_1.difference(set_2).union(set_2.difference(set_1))
