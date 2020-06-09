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
            size ([type]): [description]
            x (int, optional): [description]. Defaults to 0.
            y (int, optional): [description]. Defaults to 0.
            id ([type], optional): [description]. Defaults to None.
        """

        super().__init__(size, size, x, y, id)


    def __str__(self):
        """[str function]

        Returns:
            [type]: [Values of the Square class]
        """
        return "[Square] (%i) %i/%i - %i" % \
            (self.id, self.x, self.y, self.height)

