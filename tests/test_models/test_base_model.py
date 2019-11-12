#!/usr/bin/python3
import unittest
"""Unittest for BaseModel class"""

import unittest
from models import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittest for BaseModel class"""
    @classmethod
    def setUpClass(cls):
        """Set up instance"""
        cls.my_object = Basemodel()
        cls.my_object.name = "Diego"

    @classmethod
    def tearDown(cls):
        """Delete instance"""
        del cls.my_object

    def test_checking_for_docstring_BaseModel(self):
        """Test if all docstring were written"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_dict_BaseModel(self):
        """test dictionary as argument"""
        json_my_object = self.my_object.to_dict()
        new_object = BaseModel(**json_my_object)
        self.assertTrue(isinstance(new_object, BaseModel))
        self.assertEqual(new_object.name, "Diego")
        self.assertEqual(new_object.id, self.my_object.id)

if __name__ == '__main__':
    unittest.main()
