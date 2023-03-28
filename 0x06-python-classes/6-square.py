#!/usr/bin/python3
""" class Square: defines the class-square"""


class Square:
    """This is where the class is defined """
    def __init__(self, size=0, position=(0, 0)):
        """
        initialization
        Args:
            size(int): the size of the square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ Gets the size of the square """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Sets the size of the square """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ retrieves the position of the current square """
        return (self.__position)

    @position.setter
    def position(self, value):
        """ sets the positon of the current square """
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ Calculates the area of the sqauare """
        return (self.__size ** 2)

    def my_print(self):
        """ prints in stdout the square with the character # """
        if self.__size == 0:
            print()
        else:
            p1 = 0
            for p1 in range(self.__position[1]):
                print()
            for row in range(self.__size):
                p0 = 0
                for s in range(self.__size + self.position[0]):
                    if (p0 < self.__position[0]):
                        print(' ', end='')
                        p0 += 1
                        continue
                    print('#', end='')
                print()
