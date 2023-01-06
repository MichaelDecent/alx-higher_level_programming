#!/usr/bin/python3
""" this module contain a a function matrix_divded(matrix, div)
    which each element of the matrix is divided by div
"""

def matrix_divided(matrix, div):
    """ divides all elements of a matrix
    Args:
        matrix(list): a list of lists of integers or floats
        div(int or float): an integer or float
    Raises:
        TypeError: if the matrix has non numbers
        TypeError: if size of list in matrix is not equal
        TypeError: if divisor is not float or integer
        ZeroDivisionError: if divisor is zero

    Return:
        a new matrix with its element divided
    """
    if (not isinstance(matrix, list) or matrix == [] or 
        not all(isinstance(row, list) for row in matrix) or 
        not all((isinstance(ele, int) or isinstance(ele, float)) 
            for ele in [num for row in matrix for num in row])):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
