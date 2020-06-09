#!/usr/bin/python3
"""[Base class]"""
import json
import re


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
        if cls.__name__ == "Rectangle":
            a = cls(1, 1, 1, 1, 1)
            a.update(
                id=dictionary["id"], width=dictionary["width"],
                height=dictionary["height"], x=dictionary["x"],
                y=dictionary["y"])
            return a
        elif cls.__name__ == "Square":
            b = cls(1, 1, 1, 1)
            b.update(
                id=dictionary["id"], size=dictionary["size"],
                x=dictionary["x"], y=dictionary["y"])
            return b
        else:
            return None
