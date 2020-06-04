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

    def to_json(self, attrs=None):
        """[summary]

        Returns:
            [attrs]: [retrieves a dictionary representation]
        """
        if type(attrs) == list and all(type(x) == str for x in attrs):
            new = {}
            for i in attrs:
                if i in self.__dict__:
                    new.update({i: self.__dict__[i]})
            return new
        return self.__dict__

    def reload_from_json(self, json):
        """[summary]

        Args:
            json ([json]): [json desciption]
        """
        for i in json:
            self.__dict__.update({i: json[i]})
