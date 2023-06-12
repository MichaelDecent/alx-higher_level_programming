#!/usr/bin/python3
""" A Module that contains a class MyList that inherits from list """


class MyList(list):
    """ it inherits from list """

    def print_sorted(self):
        """ at prints the list, but
            sorted (ascending sort)
        """
        print(sorted(self))
