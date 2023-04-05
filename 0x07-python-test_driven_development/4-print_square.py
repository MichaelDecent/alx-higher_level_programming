#!/usr/bin/python3

def print_square(size):
    """ a function that prints a square with the character # 
        Args:
            size(int): size of the square
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    else:
        for row in range(size):
            for col in range(size):
                print('#', end='')
            print()
