#!/usr/bin/python3
"""[Test base for unittest]"""
from models.base import Base
import unittest
import pep8


class TestBase(unittest.TestCase):
    """[summary]

    Args:
        unittest ([type]): [description]
    """

    def test_base(self):
        """[test base]
        """
        test1 = Base()
        self.assertEqual(test1.id, 1)
        test2 = Base(12)
        self.assertEqual(test2.id, 12)
        with self.assertRaises(TypeError):
            test2 = Base(2, 2)
    
    def test_pep8(self):
        """[test pep8]
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")