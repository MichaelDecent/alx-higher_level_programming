#!/usr/bin/python3
""" class Square definition """


class Square:
    """ Represents a square """

    def __init__(self, size=0, position=(0, 0)):
        
        """ initializes the square
        Args:
            size (int): size of the square
            position (int): 
        Returns:
            None
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ getter of __size
        Returns:
            the size of the square
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ setter of __size
        Args:
            value(int):
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ getters of __position
        Returns:
            the position of the square
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """ setter of __position
        Args:
            value(tuple):
        Return:
            None
        """
        if ((type(value) is not tuple) or len(value) != 2 or \
            (type(value[0]) is not int) or \
            (type(value[1]) is not int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ Calculates the area of the square
        Return:
            The area of the square
        """
        return (self.__size ** 2)

    def my_print(self):
        """ prints the square with the character '#'
        Return:
            None
        """
        if self.__size == 0:
            print("")

        else:
            [print("") for i in range(0, self.__position[1])]
            for j in range(0, self.__size):
                [print(" ", end="") for k in range(0, self.__position[0])]
                [print('#', end="") for l in range(0, self.__size)]
                print("")
