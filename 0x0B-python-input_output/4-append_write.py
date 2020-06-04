#!/usr/bin/python3
"""[append_write function]"""


def append_write(filename="", text=""):
    """[summary]

    Args:
        filename (str, optional): [Path of file].
                  Defaults to "".
        text (str, optional): [Text to write in the file].
              Defaults to "".
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
