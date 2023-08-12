#!/usr/bin/python3
"""unittest for the User class"""
import unittest
import os
import models
from datetime import datetime
from models.user import User

class TestUser(unittest.TestCase):
    """test cases for the User class"""

    def setup(self):
        self.user = User()

    def test_has_attributes(self):
        """checking attributes of User class"""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

if __name__ == '__main__':
    unittest.main()
