#!/usr/bin/python3
"""[save_to_json_file function]"""
import json


def save_to_json_file(my_obj, filename):
    """[summary]

    Args:
        my_obj ([obj]): [object to save]
        filename ([file]): [File name]

    Returns:
        [type]: [description]
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)
