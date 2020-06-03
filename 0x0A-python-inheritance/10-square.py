#!/usr/bin/python3
"""[Square class]"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """[summary]

    Arguments:
        Rectangle {[class]} -- [class rectangle]
    """
    def __init__(self, size):
        """[initializa size]"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """[Square area]"""
        return (self.__size ** 2)
