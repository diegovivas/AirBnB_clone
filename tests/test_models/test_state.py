#!/usr/bin/python3
"""Test State Class """

from models.state import State
import datetime
import unittest


class TestUser(unittest.TestCase):
    """ Test State Class """
    my_object = State()

    def test_checking_for_docstring_User(self):
        """Test if all docstring were written"""
        self.assertIsNotNone(State.__doc__)

    def test_subclass_instance_User(self):
        """Test if my_object is a subclass of BaseModel"""
        self.assertTrue(isinstance(self.my_object, State))

    def test_attribute(self):
        """ Test attributes """
        self.assertEqual(hasattr(self.my_object, "name"), True)

if __name__ == '__main__':
    unittest.main()
