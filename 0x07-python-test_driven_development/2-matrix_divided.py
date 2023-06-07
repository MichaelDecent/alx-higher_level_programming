#!/usr/bin/python3
""" A Module that contains a function thta divides all elements in a matrix """


def matrix_divided(matrix, div):
    """  divides all elements of a matrix
        Args:
            matrix(list of list): matrix to be divide
            div(int or float): divisor
        Returns:
             a new matrix
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
    if not all([(type(row) is list) for row in matrix]):
        raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
    if not all([all([(type(ele) is int or type
                (ele) is float) for ele in row]) for row in matrix]):
        raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
    if not all([len(row) == len(matrix[1]) for row in matrix]):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    else:
        return [[round(ele / div, 2) for ele in row] for row in matrix]
