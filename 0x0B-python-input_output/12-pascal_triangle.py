#!/usr/bin/python3
"""Module containing function that prints a pascal triangle"""


def pascal_triangle(n):
    """returns a matrix of pascal triangle with height (n)"""
    if n <= 0:
        return []
    result = []

    for i in range(n):
        if i == 0:
            result.append([1])
        else:
            result.append([])
            for j in range(i + 1):
                if j == 0:
                    result[i].append(1)
                else:
                    try:
                        result[i].append(result[i - 1][j] +
                                         result[i - 1][j - 1])
                    except Exception:
                        result[i].append(1)
    return result
