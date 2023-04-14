#!/usr/bin/python3
""" This Module defines a function that returns a pascal's triangle """


def pascal_triangle(n):
    """ A function that returns a list of lists of integers
        representing the Pascal’s triangle of n:
        Args:
            n (int): the size of the pascal's triangle
        Return:  a list of lists of integers representing
        the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle = []
    for x in range(n):
        row = []
        for y in range(x + 1):
            if y == 0 or y == x:
                row.append(1)
            else:
                row.append(triangle[x-1][y-1] + triangle[x-1][y])
        triangle.append(row)

    return (triangle)
