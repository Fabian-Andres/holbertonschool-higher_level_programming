#!/urs/bin/python3
"""[lookup function]"""


def lookup(obj):
    """[Returns the list of available attributes and methods of an object]

    Arguments:
        obj {[str]} -- [list object]
    """
    return (dir(obj))
