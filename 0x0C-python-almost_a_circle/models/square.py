#!/usr/bin/python3
""" A Module that defines a class Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ inherits from class Rectangle and defines a square """
    def __init__(self, size, x=0, y=0, id=None):
        """ initialization """
        self.size = size
        self.x = x
        self.y = y
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ returns [Square] (<id>) <x>/<y> - <size> - of the square """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")

    @property
    def size(self):
        """ size getter """
        return self.__width

    @size.setter
    def size(self, new_size):
        """ size setter """
        if type(new_size) != int:
            raise TypeError("width must be an integer")
        if new_size <= 0:
            raise ValueError("width must be > 0")
        self.__width = new_size
        self.__height = new_size
    
    def update(self, *args, **kwargs):
        """ update the the values of the object attributes """
        if args and len(args) != 0:

            if len(args) >= 1:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """ returns the dictionary representation of a Square """
        square_dict = {'size': self.size, 'x': self.x, 'y': self.y, 'id': self.id}
        return (square_dict)
