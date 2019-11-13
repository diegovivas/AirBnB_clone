#!/usr/bin/python3
"""Test of City Class """

from models.city import City
import datetime
import unittest


class TestCity(unittest.TestCase):
    """ Test City Class """
    my_object = City()

    def test_checking_for_docstring_User(self):
        """Test if all docstring were written"""
        self.assertIsNotNone(City.__doc__)

    def test_subclass_instance_User(self):
        """Test if my_object 1 is a subclass of BaseModel"""
        self.assertTrue(isinstance(self.my_object, City))

    def test_attribute(self):
        """ Tests attributes"""
        self.assertEqual(hasattr(self.my_object, "state_id"), True)
        self.assertEqual(hasattr(self.my_object, "name"), True)

if __name__ == '__main__':
    unittest.main()
