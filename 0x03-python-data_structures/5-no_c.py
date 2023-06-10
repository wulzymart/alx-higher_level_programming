#!/usr/bin/env python3
def no_c(my_string):
    new_str = ""
    for _ in my_string:
        if _ != "c" and _ != "C":
            new_str += _
    return new_str
