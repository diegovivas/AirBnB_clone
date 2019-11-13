#!/usr/bin/python3
"""Test Review Class """

from models.review import Review
import datetime
import unittest


class TestReview(unittest.TestCase):
    """ Test Review Class """
    my_object = Review()

    def test_checking_for_docstring_User(self):
        """Test if all docstring were written"""
        self.assertIsNotNone(Review.__doc__)

    def test_subclass_instance_Review(self):
        """Test if my_object si a subclass of BaseModel"""
        self.assertTrue(isinstance(self.my_object, Review))

    def test_attribute_place_id(self):
        """ Tests attributes  of Review class"""
        self.assertEqual(hasattr(self.my_object, "place_id"), True)
        self.assertEqual(hasattr(self.my_object, "user_id"), True)
        self.assertEqual(hasattr(self.my_object, "text"), True)

if __name__ == '__main__':
    unittest.main()
