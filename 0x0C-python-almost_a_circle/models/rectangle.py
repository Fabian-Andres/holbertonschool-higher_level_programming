#!/usr/bin/python3
"""[Reactangle class]"""
from models.base import Base


class Rectangle(Base):
    """[Rectangle]

    Arguments:
        Base {[class]} -- [class Base]
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """[Function define the area of triangle]

        Arguments:
            width {[int]} -- [initialize width]
            height {[int]} -- [initialize height]
            x {[int]} -- [initialize x]
            y {[int]} -- [initialize y]
        """
        # self.integer_validator("width", width)
        self.__width = width
        # self.integer_validator("height", height)
        self.__height = height
        # self.integer_validator("x", x)
        self.x = x
        # self.integer_validator("y", y)
        self.__y = y
        if id is not None:
            self.id = id
        else:
            super().__init__()
        