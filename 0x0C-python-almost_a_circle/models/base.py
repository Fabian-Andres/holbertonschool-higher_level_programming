#!/usr/bin/python3
"""[Base class]"""
import json
import re
from inspect import getargspec


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
        if list_dictionaries in [None, []]:
            return "[]"

        for i in range(len(list_dictionaries)):
            if type(list_dictionaries[i]) is not dict:
                raise TypeError("The list not contain dictionaries")

        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """[from json string]

        Args:
            json_string ([str]): [json string]

        Returns:
            [type]: [returns the list of the JSON string
            representation json_string]
        """
        new_list = []
        if json_string is None or json_string == "":
            return new_list
        f = re.findall("{.*?}", json_string)
        for i in f:
            new_list.append(json.loads(i))
        return new_list

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

    @classmethod
    def create(cls, **dictionary):
        """[Create function]

        Returns:
            [type]: [returns an instance with all attributes already set]
        """
        if cls.__name__ == 'Rectangle':
            new_dict = cls(1, 1)
        elif cls.__name__ == 'Square':
            new_dict = cls(1)
        new_dict.update(**dictionary)
        return new_dict

    @classmethod
    def load_from_file(cls):
        """[Load from file function]

        Returns:
            [list]: [returns a list of instances]
        """
        new_list = []
        try:
            with open("%s.json" % cls.__name__, mode='r') as f:
                file = cls.from_json_string(f.read())
                for i in file:
                    new_list.append(cls.create(**i))
        except Exception:
            pass
        return new_list
