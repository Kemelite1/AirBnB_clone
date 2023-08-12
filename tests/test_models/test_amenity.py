#!/usr/bin/python3
"""unittest for the Amenity class"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """test cases for Amenity class"""

    amenity = Amenity()

    def test_has_attribute(self):
        """checking attributes of Amenity class"""
        self.assertTrue(hasattr(self.amenity, 'name'))


if __name__ == '__main__':
    unittest.main()
