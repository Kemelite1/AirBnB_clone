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

    def test_init_new_instance(self):
        """Tests whether a new instance of State class is created correctly and if attributes are set as expected"""
        self.assertIsInstance(self.state, State)
        self.assertIsNotNone(self.state.id)
        self.assertIsInstance(self.state.created_at, datetime)
        self.assertIsInstance(self.state.updated_at, datetime)
        self.assertEqual(self.state.created_at, self.state.updated_at)

    def test_has_attribute(self):
        """checking attributes of State class"""
        self.assertTrue(hasattr(self.state, 'name'))

    def test_init_with_kwargs(self):
        """Test initialization of State instance with keyword arguments and verifies attribute values"""
        state_data = {
            'id': '445577',
            'created_at': '2023-08-01T12:34:56.789012',
            'updated_at': '2023-08-01T12:34:56.789012',
            'name': 'Lagos'
        }
        state_instance = State(**state_data)
        self.assertIsInstance(state_instance, State)
        self.assertEqual(state_instance.id, '445577')
        self.assertEqual(state_instance.name, 'Lagos')
        self.assertIsInstance(state_instance.created_at, datetime)
        self.assertIsInstance(state_instance.updated_at, datetime)

    def test_save_method(self):
        """Tests the save method to ensure that the updated_at attribute changes after calling save"""
        prev_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(prev_updated_at, self.state.updated_at)

    def test_to_dict_method(self):
        """Tests the to_dict method to ensure that the dictionary representation is created correctly with the expected attributes"""
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict['id'], self.state.id)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertIsInstance(state_dict['created_at'], str)
        self.assertIsInstance(state_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()
