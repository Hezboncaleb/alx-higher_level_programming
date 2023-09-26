#!/usr/bin/python3
""" Script defining class square """


class Square:
    """ Defines a class square """
    def __init__(self, size=0):
        """ Initializing a square class
        Args: size=0: size of the square
         """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Calculates the area of the square """
        return self.__size ** 2
