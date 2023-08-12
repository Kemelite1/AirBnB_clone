#!/usr/bin/python3
"""unittest for the State class"""
import unittest
import os
import models
from datetime import datetime
from models.state import State

class TestState(unittest.TestCase):
    """test cases for State class"""

    def setup(self):
        self.state = State()

    def test_has_attribute(self):
        """checking attributes of State class"""
        self.assertTrue(hasattr(self.state, 'name'))


if __name__ == '__main__':
    unittest.main()
