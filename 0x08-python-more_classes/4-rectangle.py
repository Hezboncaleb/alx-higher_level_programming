#!/usr/bin/python3
"""Creates a Rectangle class"""


class Rectangle:
    """Defines a class rectangle"""

    def __init__(self, width=0, height=0):

        """Initializes a  Rectangle"""

        self.__width = 0
        self.__height = 0
        self.width = width
        self.height = height

    @property
    def width(self):
        """sets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not type(int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """sets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not type(int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Computes the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Computes the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
            return (self.width + self.height) * 2

    def __str__(self):
        """Prints the rectangle """
        if self.width == 0 or self.height == 0:
            return ""
        return ((("#" * self.width) + "\n") * self.height)[:-1]

    def __repr__(self):
        """Prints the rectangle using eval"""
        return "Rectangle({}, {})".format(self.width, self.height)
