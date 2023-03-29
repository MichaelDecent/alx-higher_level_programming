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
        if (not isinstance(value, int)):
            raise TypeError('data must be an integer')
        else:
            self._data = value

    @property
    def next_node(self):
        """It Retrieves the next_node
            Returns: the next_node
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, node):
        """ Sets a node
            Args:
                node(object): the node to set
        """
        if (node is not None and not isinstance(node, Node)):
            raise TypeError('next_node must be a Node object')
        self.__next_node = node


class SinglyLinkedList:
    """  defines a singly linked list """
    def __init__(self):
        """ Initialization """
        self.head = None

    def __str__(self):
        """ Printing the list """
        slist = ""
        temp = self.head
        while temp:
            slist += str(temp.data) + "\n"
            temp = temp.next_node
        return slist[:-1]

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted
        position in the list (increasing order)
            Args:
                value: what the value will be on the node
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        if self.head.data > value:
            new_node.next_node = self.head
            self.head = new_node
            return
        temp = self.head
        while temp.next_node and temp.next_node.data < value:
            temp = temp.next_node
        if temp.next_node:
            new_node.next_node = temp.next_node
        temp.next_node = new_node
