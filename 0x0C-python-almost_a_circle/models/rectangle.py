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
        self.width = width
        self.integer_validator("width", width)
        self.height = height
        self.integer_validator("height", height)
        self.x = x
        self.integer_validator("x", x)
        self.y = y
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
        return self.width * self.height

    def display(self):
        """[Function prints in stdout the Rectangle]
        """
        for j in range(self.x):
            print()
        for i in range(self.height):
            for k in range(self.y):
                print(" ", end="")
            for y in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """[str function]

        Returns:
            [type]: [Values of the rectangle class]
        """
        return "[rectangle] (%i) %i/%i - %i/%i" % \
            (self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """[Function update]
        """
        a = 0
        for i in range(len(args)):
            a += 1
            if i == 0:
                self.id = args[i]
            elif i == 1:
                self.width = args[i]
            elif i == 2:
                self.height = args[i]
            elif i == 3:
                self.x = args[i]
            elif i == 4:
                self.y = args[i]
            else:
                return

        if a == 0:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if key == "id":
                        self.id = value
                    elif key == "width":
                        self.width = value
                    elif key == "height":
                        self.height = value
                    elif key == "x":
                        self.x = value
                    elif key == "y":
                        self.y = value

    def to_dictionary(self):
        """[Dictionary function]
        """
        d = dict()
        d["id"] = self.id
        d["width"] = self.width
        d["height"] = self.height
        d["x"] = self.x
        d["y"] = self.y
        return d
