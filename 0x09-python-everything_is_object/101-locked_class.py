#!/usr/bin/python3
""" Defining locked class """


class LockedClass:
    """ The class prevents user from
    dynamically new attributes """
    __slots__ = ['first_name']
