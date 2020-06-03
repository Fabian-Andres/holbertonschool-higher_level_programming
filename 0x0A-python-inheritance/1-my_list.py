#!/usr/bin/python3
"""[MyList Class]"""


class MyList(list):
    """[Class that prints the sorted list]
    """
    def print_sorted(self):
        """[print_sorted function]
        """
        print(sorted(self))
