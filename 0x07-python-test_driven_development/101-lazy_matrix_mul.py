#!/usr/bin/python3
"""Module containing lazy matrix multiplication function"""


from numpy import matmul


def lazy_matrix_mul(m_a, m_b):
    """Multiplies 2 matrixes

    Args:
        m_a (list of int or float lists): first matrix
        m_b (list of int or float lists): second matrix

    Returns a single matrix
    """
    return (matmul(m_a, m_b))
