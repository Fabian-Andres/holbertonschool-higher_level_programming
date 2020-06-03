#!/usr/bin/python3
"""[BaseGeometry class]"""


class BaseGeometry:
    """[BaseGeometry class]
    """
    def area(self):
        """
        Raises:
            Exception: [area() is not implemented]
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """[integer_validator]
            Raises:
            Exception: [return exception]
        """
        if type(value) != int:
            raise Exception("{} must be an integer".format(name))
        elif value <= 0:
            raise Exception("{} must be greater than 0".format(name))
