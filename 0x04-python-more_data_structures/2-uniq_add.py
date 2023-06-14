#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    if my_list:
        for _ in set(my_list):
            sum += _
    return sum
