#!/usr/bin/python3
"""Module contains function for matrix division"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix.

    Args:
        matrix (list of list of integers or float): Matrix to be divided
        div (int or float): divisor

    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size
        TypeError: div must be a number
        ZeroDivisionError: division by zero

    Returns: A new matrix containing results of division in 2 decimal places
    """
    if not matrix or not isinstance(matrix, list) or\
        not all(row and isinstance(row, list) for row in matrix) or\
            not all(((isinstance(num, int) or isinstance(num, float)) and
                    (float('-inf') < float(num) < float('inf')))
                    for num in [nums for row in matrix for nums in row]):
        raise TypeError("matrix must be a matrix (list of lists) of\
 integers/floats")
    len_row1 = len(matrix[0])
    if not all(len(row) == len_row1 for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if (not isinstance(div, float) and not isinstance(div, int)) or\
            not (float('-inf') < float(div) < float('inf')):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [list(map(lambda num: round(num / div, 2), row)) for row in matrix]
