#!/usr/bin/python3
def max_integer(my_list=[]):
    max = None if not my_list else my_list[1]
    if my_list:
        for _ in my_list:
            max = _ if _ > max else max
    return max
