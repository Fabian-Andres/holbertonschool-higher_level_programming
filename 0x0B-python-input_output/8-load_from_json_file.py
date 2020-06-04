#!/usr/bin/python3
"""[load_from_json_file function]"""
import json


def load_from_json_file(filename):
    """[summary]

    Args:
        filename ([file]): [File for create object]
    """
    with open(filename, encoding="utf-8") as file:
        return json.load(file)
