#!/usr/bin/python3
"""[MyList]"""


class MyList(list):
    """[MyList Class]

    Arguments:
        list {[type]} -- [Class that prints the sorted list]
    """
    def print_sorted(self):
        print(sorted(self))
