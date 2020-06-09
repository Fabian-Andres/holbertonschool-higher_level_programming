#!/usr/bin/python3
"""[Reactangle class]"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """[summary]

    Args:
        Rectangle ([class]): [Triangle class]
    """

    def __init__(self, size, x=0, y=0, id=None):
        """[summary]

        Args:
            size ([type]): [size of square]
            x (int, optional): [initialize position x].
                Defaults to 0.
            y (int, optional): [initialize position x].
                Defaults to 0.
            id ([type], optional): [id of base]. Defaults to None.
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """[str function]

        Returns:
            [type]: [Values of the Square class]
        """
        return "[Square] (%i) %i/%i - %i" % \
            (self.id, self.x, self.y, self.height)

    @property
    def size(self):
        """[Size property]

        Returns:
            [type]: [size square]
        """
        return self.width

    @size.setter
    def size(self, value):
        """[Size seter]

        Args:
            value ([int]): [Value size of higth and with]
        """
        self.width = value
        self.height = value
