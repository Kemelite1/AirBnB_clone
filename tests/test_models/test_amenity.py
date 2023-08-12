#!/usr/bin/python3
"""unittest for the Amenity class"""
import unittest
import os
import models
from datetime import datetime
from models.amenity import Amenity

class TestPlace(unittest.TestCase):
    """test cases for Amenity class"""

    def setup(self):
        self.amenity = Amenity()

    def test_has_attribute(self):
        """checking attributes of Amenity class"""
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))

if __name__ == '__main__':
    unittest.main()
