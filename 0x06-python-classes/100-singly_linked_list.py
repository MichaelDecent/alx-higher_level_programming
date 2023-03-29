#!/usr/bin/python3
""" class Node: defines a node of a singly linked list by """
class Node:
    """ this is where the node of a linked list is defined """
    def __init__(self, data, next_node=None):
        """ Initaialization
            Args:
                data(int): the data to added to the list
                next_node(object): node to be added to a linked list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Retrieves the data of the list
            Returns: the data
        """
        return (self._data)
    @data.setter
    def data(self, value):
        """ sets the data of the list
        Args:
            value(int): the value used to set the data to
        """
        if type(value) is not int:
            raise TypeError('data must be an integer')
        else:
            self._data = value

    @property
    def next_node(self):
        """It Retrieves the number




