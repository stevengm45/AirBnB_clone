#!/usr/bin/python3
"""
   Place tests
"""
from models.place import Place
import unittest


class TestPlace(unittest.TestCase):
    """
       Unittest for class Place - class Place
    """
    def test_instantiation(self):
        """Test to prove the instantiation of an
        object class Amenity
        """
        instance = Place()
        self.assertEqual(Place, type(instance))

    def test_id(self):
        """Test to prove that ids are different"""
        id_a = Place()
        id_b = Place()
        self.assertNotEqual(id_a, id_b)

    def test__str__(self):
        """Test to prove that the return is a string"""
        instance = Place()
        self.assertTrue(instance.__str__(), type(str))

    def test_to_save(self):
        """Test to prove the datatime of creation and update
        """
        instance = Place()
        old_date_created = instance.created_at
        old_date_updated = instance.updated_at
        instance.save()
        new_date_created = instance.created_at
        new_date_updated = instance.updated_at
        self.assertEqual(old_date_created, new_date_created)
        self.assertNotEqual(old_date_updated, new_date_updated)

    def test_to_dict(self):
        """Test to prove if the return is type dict and the
           values are different
        """
        model_a = Place()
        model_b = Place()
        model_dict_a = model_a.to_dict()
        model_dict_b = model_b.to_dict()
        self.assertNotEqual(model_a.created_at, model_b.created_at)
        self.assertNotEqual(model_a.updated_at, model_b.updated_at)
        self.assertTrue(model_dict_a, type(dict))
        self.assertTrue(model_dict_b, type(dict))

if __name__ == '__main__':
    unittest.main()