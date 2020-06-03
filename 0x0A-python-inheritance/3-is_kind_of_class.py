#!/usr/bin/python3
"""[is_kind_of_class function]"""


def is_kind_of_class(obj, a_class):
    """[is kind of class]

    Arguments:
        obj {[object]} -- [object to compare]
        a_class {[instance]} -- [instance to compare]

    Returns:
        [bol] -- [return true if or false]
    """
    return isinstance(obj, a_class)
