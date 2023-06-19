#!/usr/bin/python3
""" This MOdule contain class Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ the prototype for individul square """
    def __init__(self, size, x=0, y=0, id=None):
        """ initialization """
        super().__init__(size, size, x, y, id)
        self.size = size
        self.x = x
        self.y = y

    @property
    def size(self):
        """ getter for size """
        return self.__width

    @size.setter
    def size(self, new_size):
        """ setter for size """
        if type(new_size) is not int:
            raise TypeError("width must be an integer")
        if new_size < 0:
            raise ValueError("width must be > 0")
        self.__height = new_size
        self.__width = new_size

    def __str__(self):
        """ returns '[Square] (<id>) <x>/<y> - <size>' """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")

    def update(self, *args, **kwargs):
        """ update the attributes of the class """
        if args and len(args) != 0:
            for n, arg in enumerate(args):
                if n == 0:
                    self.id = arg
                elif n == 1:
                    self.size = arg
                elif n == 2:
                    self.x = arg
                elif n == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """  returns the dictionary representation of a Square """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
