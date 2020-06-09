#!/usr/bin/python3
"""[Base class]"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """[summary]

        Args:
            list_dictionaries ([type]): [list of dictionaries]

        Raises:
            TypeError: [The list not contain dictionaries]

        Returns:
            [dict]: [JSON string representation of list_dictionaries]
        """
        if not list_dictionaries:
            return "[]"

        for i in range(len(list_dictionaries)):
            if type(list_dictionaries[i]) is not dict:
                raise TypeError("The list not contain dictionaries")

        new_json = "["
        for j in range(len(list_dictionaries)):
            if j < i:
                new_json += json.dumps(list_dictionaries[j]) + ", "
            else:
                new_json += json.dumps(list_dictionaries[j])
        new_json += "]"
        return new_json

    @classmethod
    def save_to_file(cls, list_objs):
        """[save to file function]

        Args:
            list_objs ([type]): [Objects list to write]
        """
        l = []
        if list_objs is not None:
            for item in list_objs:
                l.append(item.to_dictionary())
        with open("%s.json" % cls.__name__, mode='w') as f:
            f.write(Base.to_json_string(l))
