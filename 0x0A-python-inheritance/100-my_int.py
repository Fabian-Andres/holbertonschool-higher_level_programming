#!/usr/bin/python3
"""[MyInt function]"""


class MyInt (int):
    """[Class MyInt that inherits from int]"""
    def __eq__(self, other):
        """Extrange equal"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Extrange no-equal"""
        return super().__eq__(other)
