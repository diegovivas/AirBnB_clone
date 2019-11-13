#!/usr/bin/python3
"""Test Place Class """

from models.place import Place
import datetime
import unittest


class TestPlace(unittest.TestCase):
    """ Test Place Class """
    my_object = Place()

    def test_checking_for_docstring(self):
        """Test if all docstring were written"""
        self.assertIsNotNone(Place.__doc__)

    def test_instance(self):
        """Test if my_object is a subclasses of BaseModel"""
        self.assertTrue(isinstance(self.my_object, Place))

    def test_attribute_city_id(self):
        """ Tests attributes """
        self.assertEqual(hasattr(self.my_object, "city_id"), True)
        self.assertEqual(hasattr(self.my_object, "user_id"), True)
        self.assertEqual(hasattr(self.my_object, "name"), True)
        self.assertEqual(hasattr(self.my_object, "description"), True)
        self.assertEqual(hasattr(self.my_object, "number_rooms"), True)
        self.assertEqual(hasattr(self.my_object, "number_bathrooms"), True)
        self.assertEqual(hasattr(self.my_object, "max_guest"), True)
        self.assertEqual(hasattr(self.my_object, "price_by_night"), True)
        self.assertEqual(hasattr(self.my_object, "latitude"), True)
        self.assertEqual(hasattr(self.my_object, "longitude"), True)
        self.assertEqual(hasattr(self.my_object, "amenity_ids"), True)

if __name__ == '__main__':
    unittest.main()
