#!/usr/bin/python3
"""unittest for the Review class"""
import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """test cases for Review class"""

    review = Review()

    def test_has_attribute(self):
        """checking attributes of review class"""
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))

if __name__ == '__main__':
    unittest.main()
