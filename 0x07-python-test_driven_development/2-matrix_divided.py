#!/usr/bin/python3
""" Module that divides all the element in the list """


def matrix_divided(matrix, div):
    """ a function that divides all elements of a matrix
        Args:
            matrix(list): list of list
            div(i): value to divide with
        Returns: a new matrix
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    if all([type(row) == list for row in matrix]) is False:
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    if all([all([(type(col) == int or type(col) == float) 
        for col in row]) for row in matrix]) is False:
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    if all([len(matrix[0]) == len(row) for row in matrix]) is False:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([[round((col / div), 2) for col in row] for row in matrix])
