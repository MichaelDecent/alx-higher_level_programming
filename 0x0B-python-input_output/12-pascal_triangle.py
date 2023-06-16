#!/usr/bin/python3
""" This Module contains a function hat returns a list
    of lists of integers representing the Pascal’s triangle
"""


def pascal_triangle(n):
    """  returns a list of lists of integers
        representing the Pascal’s triangle of n
        Args:
            n(int): size of the pascal triangle
    """
    triangle = []
    if n <= 0:
        return triangle

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j > 0 and j < i:
                row.append(triangle[i - 1][j] + triangle[i - 1][j - 1])
            else:
                row.append(1)
        triangle.append(row)
    return triangle
