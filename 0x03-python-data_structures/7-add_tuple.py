#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = b = 0
    for tuple_t in (tuple_a, tuple_b):
        lenth = len(tuple_t)
        if lenth > 0:
            a += tuple_t[0]
        if lenth > 1:
            b += tuple_t[1]
    return (a, b)
