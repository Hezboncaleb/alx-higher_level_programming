#!/usr/bin/python3
""" Script defining a square class """


class Square:
    """ Defines a class square """
    def __init__(self, size=0):
        """ Initializing a square class
        Args: size=0: size of the square
         """
        self.__size = size

    @property
    def size(self):
        """ Gets the size of the square """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setting the size of the square """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Computes the area of the square """
        return (self.__size ** 2)
