#!/usr/bin/python3
"""[read_file function]"""


def number_of_lines(filename=""):
    """[function that print content of file]

    Keyword Arguments:
        filename {str} -- [String to prints it to stdout:]
        (default: {""})
    """
    with open(filename, encoding="utf-8") as file:
        return len(file.readlines())
