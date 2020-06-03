#!/usr/bin/python3
"""[read_file function]"""


def read_file(filename=""):
    """[function that print content of file]

    Keyword Arguments:
        filename {str} -- [String to prints it to stdout:]
        (default: {""})
    """
    with open(filename, 'r') as f:
        read_data = f.read()

    print(read_data)
