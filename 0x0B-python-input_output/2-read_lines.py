#!/usr/bin/python3
"""[read_lines function]"""


def read_lines(filename="", nb_lines=0):
    """[summary]

    Args:
        filename (str, optional): [String to prints it to stdout].
                  Defaults to "".
        nb_lines (int, optional): [Number of lines to read].
                  Defaults to 0.
    """
    with open(filename, encoding="utf-8") as file:
        if nb_lines <= 0:
            print(file.read(), end="")
        else:
            for line in range(nb_lines):
                print(file.readline(), end="")
