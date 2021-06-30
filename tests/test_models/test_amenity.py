#!/usr/bin/python3
"""
   Amenity tests
"""
from models.base_model import BaseModel
import models
import unittest


class TestAmenity(unittest.TestCase):
    """
       Unittest for class Amenity - class Amenity
    """
    def test_id(self):
        """Test to prove that ids are different"""
        id_a = BaseModel()
        id_b = BaseModel()
        self.assertNotEqual(id_a, id_b)

    def test__str__(self):
        """Test to prove that the return is a string"""
        instance = BaseModel()
        self.assertTrue(instance.__str__(), type(str))

    def test_to_save(self):
        instance = BaseModel()
        old_date_created = instance.created_at
        old_date_updated = instance.updated_at
        instance.save()
        new_date_created = instance.created_at
        new_date_updated = instance.updated_at
        self.assertNotEqual(old_date_updated, new_date_updated)

    def test_to_dict(self):
        """Test to prove if the return is type dict and the
           values are different
        """
        model_a = BaseModel()
        model_b = BaseModel()
        model_dict_a = model_a.to_dict()
        model_dict_b = model_b.to_dict()
        self.assertNotEqual(model_a.created_at, model_b.created_at)
        self.assertNotEqual(model_a.updated_at, model_b.updated_at)
        self.assertTrue(model_dict_a, type(dict))
        self.assertTrue(model_dict_b, type(dict))

if __name__ == '__main__':
    unittest.main()
