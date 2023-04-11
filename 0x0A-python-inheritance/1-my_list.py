#!/usr/bin/python3
""" This Module that inherits from list """


class MyList(list):
    """ class MyList that inherits from list """
    def print_sorted(self):
        """ A method that prints the list,
            but sorted (ascending sort)
        """
        print(sorted(self))
