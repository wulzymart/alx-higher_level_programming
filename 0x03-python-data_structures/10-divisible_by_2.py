#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    truth_list = []
    for _ in my_list:
        truth_list.append(True if _ % 2 == 0 else False)
    return truth_list
