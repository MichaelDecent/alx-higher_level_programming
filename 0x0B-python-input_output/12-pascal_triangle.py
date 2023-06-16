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
    if n <= 0:
        return []

    final = []
    for i in range(n):
        triangle = []
        for j in range(i + 1):
            if j > 0 and j < i:
                triangle.append(final[i - 1][j] + final[i - 1][j - 1])
            else:
                triangle.append(1)
        final.append(triangle)
    return final
