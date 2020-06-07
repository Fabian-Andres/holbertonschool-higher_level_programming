#!/usr/bin/python3
"""[Base class]"""


class Base:
    """[Base]
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """[summary]

        Args:
            id ([int], optional): [id of base].
            Defaults to None.
        """
        self.id = id

        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
    