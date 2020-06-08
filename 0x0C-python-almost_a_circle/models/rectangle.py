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
            x {[int]} -- [initialize position x]
            y {[int]} -- [initialize coordinate y]
        """
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)
        self.__x = x
        self.integer_validator("x", x)
        self.__y = y
        self.integer_validator("y", y)
        if id is not None:
            self.id = id
        else:
            super().__init__()

    @staticmethod
    def integer_validator(name, value):
        """[Function for integers validation]

        Args:
            name ([str]): [description]
            value ([type]): [Value to validate ]

        Raises:
            TypeError: [must be an integer]
            ValueError: [must be >= 0]
        """

        if type(value) != int:
            raise TypeError("%s must be an integer" % name)

        if name == "x" or name == "y":
            if value < 0:
                raise ValueError("%s must be >= 0" % name)
        else:
            if value <= 0:
                raise ValueError("%s must be > 0" % name)

    def area(self):
        """[Function area]

        Returns:
            [int]: [return area of rectangle]
        """
        return self.__width * self.__height

    def display(self):
        """[Function prints in stdout the Rectangle]
        """
        for j in range(self.__x):
            print()
        for i in range(self.__height):
            for k in range(self.__y):
                print(" ", end="")
            for y in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """[str function]

        Returns:
            [type]: [Values of the rectangle class]
        """
        return "[rectangle] (%i) %i/%i - %i/%i" % \
            (self.id, self.__x, self.__y, self.__width, self.__height)
