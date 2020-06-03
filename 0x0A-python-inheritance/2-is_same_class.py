#!/usr/bin/python3
"""[is_same_class function]"""


def is_same_class(obj, a_class):
    """[If same class]

    Arguments:
        obj {[object]} -- [object to compare]
        a_class {[instance]} -- [instance to compare]

    Returns:
        [bol] -- [return true if the object is exactly an
        instance or false]
    """

    return (type(obj) == a_class)
