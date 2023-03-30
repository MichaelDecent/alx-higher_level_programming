#!/usr/bin/python3
"""class Square: that defines a square by"""


class Square:
    """ definition of a square """
    def __init__(self, size=0, position=(0, 0)):
        """ Initialization
            Args:
                size(int): size of the square
                position(Tuple): it defines the position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ A getter for size of the square """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ A setter for the Square
            Args:
                value: the value of the new size of square
       """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        """ a getter for the position of the square """
        return (self.__position)

    @position.setter
    def position(self, value):
        """ A setter for the position of the square
            Args:
                value(tuple): it define the position of the square
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not isinstance(value[0], int) or not isinstance(value[1], int) \
           or value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integer')
        else:
            self.__position = value

    def area(self):
        """ Area of the square
            Returns: the area of the square
        """
        return (self.__size ** 2)

    def my_print(self):
        """ that prints in stdout the square with the character # """
        if self.__size == 0:
            print()
        else:
            for p1 in range(self.__position[1]):
                print()
            for row in range(self.__size):
                p2 = 0
                for s in range(self.__size + self.__position[0]):
                    if p2 < self.__position[0]:
                        print(' ', end='')
                        p2 += 1
                    print('#', end='')
                print()

    def __str__(self):
        """ prints the square """
        sq_str = ""
        if self.__size == 0:
            return
        else:
            for p1 in range(self.__position[1]):
                sq_str += '\n'
            for row in range(self.__size):
                p2 = 0
                for s in range(self.__size + self.__position[0]):
                    if p2 < self.__position[0]:
                        sq_str += ' '
                        p2 += 1
                        continue
                    sq_str += '#'
                sq_str += '\n'

        return (sq_str[:-1])
