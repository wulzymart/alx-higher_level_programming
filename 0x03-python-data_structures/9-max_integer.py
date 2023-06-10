#!/usr/bin/python3
def max_integer(my_list=[]):
    max = None
    if my_list:
        max = my_list[0]
        for _ in my_list:
            if _ > max:
                max = _
    return max
