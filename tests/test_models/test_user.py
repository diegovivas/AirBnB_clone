#!/usr/bin/python3
"""Test of User Class """

from models.user import User
import datetime
import unittest


class TestUser(unittest.TestCase):
    """ Test User Class """
    my_object = User()
    my_object.name = "Diego"

    def test_checking_for_docstring_User(self):
        """Test if all docstring were written"""
        self.assertIsNotNone(User.__doc__)

    def test_subclass_instance_User(self):
        """Test if my_object is a subclasses of BaseModel"""
        self.assertTrue(isinstance(self.my_object, User))

    def test_attribute_city(self):
        """Test attributes of User class"""
        self.assertTrue(hasattr(self.my_object, 'email'))
        self.assertTrue(hasattr(self.my_object, 'password'))
        self.assertTrue(hasattr(self.my_object, 'first_name'))
        self.assertTrue(hasattr(self.my_object, 'last_name'))

if __name__ == '__main__':
    unittest.main()
