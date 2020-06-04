#!/usr/bin/python3
"""[to_json_string function]"""
import json


def from_json_string(my_str):
    """[summary]

    Args:
        my_obj ([obj]): [object]

    Returns:
        [type]: [returns the JSON representation of an object (string)]
    """
    return json.loads(my_str)
