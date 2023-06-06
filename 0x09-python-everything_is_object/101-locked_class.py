#!/usr/bin/python3
"""  class LockedClass describes a locked class """


class LockedClass:
    """ allows the access to only one attribute """
    __slots__ = ["first_name"]
