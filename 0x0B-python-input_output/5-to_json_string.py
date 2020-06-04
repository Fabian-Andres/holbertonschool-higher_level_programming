#!/usr/bin/python3
"""[to_json_string function]"""
import json


def to_json_string(my_obj):
    """[summary]

    Args:
        my_obj ([obj]): [object]

    Returns:
        [type]: [returns the JSON representation of an object (string)]
    """
    return json.dumps(my_obj)
