#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = 0
    total_weight = 0
    if my_list:
        for score, weight in my_list:
            sum += score * weight
            total_weight += weight
    return sum / total_weight if total_weight else 0
