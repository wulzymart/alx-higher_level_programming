#!/usr/bin/python3
"""Module containing matrix multiplication"""


def matrix_mul(m_a, m_b):
    """Multiplies 2 matrixes

    Args:
        m_a (list of int or float lists): first matrix
        m_b (list of int or float lists): second matrix

    Raises:
        TypeError: if any parameter not a list or not list of lists\
 or not containing ntegers or floats or not inner lists are not of equal size
        ValueError if either list or content of lists empty

    Returns a single matrix
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError(
            "m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all(isinstance(num, int) or isinstance(num, float) for num in
               [nums for row in m_a for nums in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(num, int) or isinstance(num, float) for num in
               [nums for row in m_b for nums in row]):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    len_m_a = len(m_a)
    len_m_b = len(m_b)
    len_m_b_0 = len(m_b[0])
    result = []
    for _ in range(len_m_a):
        result.append([0] * len_m_b_0)
    for i in range(len_m_a):
        for j in range(len_m_b_0):
            for k in range(len_m_b):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return (result)


if __name__ == "__main__":
    m_a = [
        [2, 2],
        [2, 4],
    ]
    m_b = m_a
    print(matrix_mul(m_a, m_b))
    matrix_mul()
