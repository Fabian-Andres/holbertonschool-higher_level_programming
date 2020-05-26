#!/usr/bin/python3
""" This is Rectangle Class """


class Rectangle:
    """ Define the width and height """
    def __init__(self, width=0, height=0):
        """ Initialization of attributes for width and height """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ @property for width """
        return self.__width

    @property
    def height(self):
        """ @property for height """
        return self.__height

    @width.setter
    def width(self, value):
        """ @width.setter attribute """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ @height.setter attribute """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
