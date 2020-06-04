#!/usr/bin/python3
"""[write_file function]"""


def write_file(filename="", text=""):
    """[summary]

    Args:
        filename (str, optional): [Path of file].
                  Defaults to "".
        text (str, optional): [Text to write in the file].
              Defaults to "".
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
