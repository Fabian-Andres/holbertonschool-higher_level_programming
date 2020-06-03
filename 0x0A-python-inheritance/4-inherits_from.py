#!/usr/bin/python3
"""[inherits_from function]"""


def inherits_from(obj, a_class):
    """[inherits]

    Arguments:
        obj {[bol]} -- [True or False for comparation]
        a_class {[type]} -- [Type of class]

    Returns:
        [bol] -- [return true if or false]
    """
    return (type(obj) != a_class and issubclass(type(obj), a_class))
