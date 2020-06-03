#!/usr/bin/python3
"""[Rectangle class]"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """[Rectangle]

    Arguments:
        BaseGeometry {[class]} -- [class BaseGeometry]
    """
    def __init__(self, width, height):
        """[summary]

        Arguments:
            width {[int]} -- [initialize width]
            height {[int]} -- [initialize height]
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
