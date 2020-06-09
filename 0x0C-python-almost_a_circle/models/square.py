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
