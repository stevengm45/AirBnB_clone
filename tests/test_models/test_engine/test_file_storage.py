#!/usr/bin/python3
"""
   FileStorage tests
"""
import models
import unittest


class TestFileStorage(unittest.TestCase):
    """
       Unittest for class FileStorage - class FileStorage
    """
    def test_instance(self):
        """Test to prove the instantiation of an
        object class Amenity
        """
        instance = models.FileStorage()
        self.assertTrue(models.FileStorage, type(instance))

    def test_all(self):
        """Test the method all to print dict"""
        obj = models.storage.all()
        self.assertTrue(dict, type(obj))

if __name__ == '__main__':
    unittest.main()
