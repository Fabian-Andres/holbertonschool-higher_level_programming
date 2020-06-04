#!/usr/bin/python3
"""[class_to_json function]"""


def class_to_json(obj):
    """[summary]

    Args:
        obj ([obj]): [Object]

    Returns:
        [type]: [dict]
    """
    return obj.__dict__
