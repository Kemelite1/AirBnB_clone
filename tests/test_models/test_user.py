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

    def test_init_new_instance(self):
        """Checks whether a new instance of User class is created correctly and if attributes are set as expected"""
        self.assertIsInstance(self.user, User)
        self.assertIsNotNone(self.user.id)
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertIsInstance(self.user.updated_at, datetime)
        self.assertEqual(self.user.created_at, self.user.updated_at)

    def test_has_attributes(self):
        """checking attributes of User class"""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_init_with_kwargs(self):
        """Tests initialization of User instance with keyword arguments and verifies attribute values"""
        user_data = {
            'id': '445566',
            'created_at': '2023-08-01T12:34:56.789012',
            'updated_at': '2023-08-01T12:34:56.789012',
            'email': 'unittest@user.com',
            'password': '123456',
            'first_name': 'Kumdan',
            'last_name': 'Keme'
        }
        user_instance = User(**user_data)
        self.assertIsInstance(user_instance, User)
        self.assertEqual(user_instance.id, '445566')
        self.assertEqual(user_instance.email, 'unittest@user.com')
        self.assertEqual(user_instance.first_name, 'Kumdan')
        self.assertEqual(user_instance.last_name, 'Keme')
        self.assertIsInstance(user_instance.created_at, datetime)
        self.assertIsInstance(user_instance.updated_at, datetime)

    def test_save_method(self):
        """Tests the save method to ensure that the updated_at attribute changes after calling save"""
        prev_updated_at = self.user.updated_at
        self.user.save()
        self.assertNotEqual(prev_updated_at, self.user.updated_at)

    def test_to_dict_method(self):
        """Tests the to_dict method to ensure that the dictionary representation is created correctly with the expected attributes"""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['id'], self.user.id)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertIsInstance(user_dict['created_at'], str)
        self.assertIsInstance(user_dict['updated_at'], str)


if __name__ == '__main__':
    unittest.main()
