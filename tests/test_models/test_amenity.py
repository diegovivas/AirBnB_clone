#!/usr/bin/python3
"""
Test Amenity Class
"""

from models.amenity import Amenity
import datetime
import unittest


class TestAmenity(unittest.TestCase):
    """ Test Amenity Class """
    my_object = Amenity()

    def test_checking_for_docstring(self):
        """Test if all docstring were written"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_subclass_instance_User(self):
        """Test if my_object is a subclass of BaseModel"""
        self.assertTrue(isinstance(self.my_object, Amenity))

    def test_attribute_name(self):
        """Check attributes"""
        self.assertEqual(hasattr(self.my_object, 'name'), True)

if __name__ == '__main__':
    unittest.main()
