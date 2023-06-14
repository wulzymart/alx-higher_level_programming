#!/usr/bin/python3
def best_score(a_dictionary):
    best = None
    innital = 0
    if a_dictionary:
        best_val = list(a_dictionary.values())[0]
        for key, value in a_dictionary.items():
            if value >= best_val:
                best = key
                best_val = value
    return best
