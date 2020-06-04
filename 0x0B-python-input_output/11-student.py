#!/usr/bin/python3
"""[Student class]"""


class Student():
    """[summary]
    """
    def __init__(self, first_name, last_name, age):
        """[Constructor]"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """[summary]

        Returns:
            [dic]: [retrieves a dictionary representation ]
        """
        return self.__dict__
