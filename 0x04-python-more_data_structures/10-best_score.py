#!/usr/bin/python3
def best_score(a_dictionary):
    best = None
    innital = 0
    if a_dictionary:
        for key, value in a_dictionary.items():
            best = key if value >= innital else best
            innital = value
    return best
