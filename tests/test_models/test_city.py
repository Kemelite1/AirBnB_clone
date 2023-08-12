#!/usr/bin/python3
"""unittest for the State class"""
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """test cases for City class"""

    
    city = City()

    def test_has_attribute(self):
        """checking for attributes of City class"""
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))


if __name__ == '__main__':
    unittest.main()
