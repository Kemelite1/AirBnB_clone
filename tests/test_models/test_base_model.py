#!/usr/bin/python3
"""unittest for the BaseModel class"""

import unittest
import models
import os
import json
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """unittests to test the for the BaseModel class"""

    def test_init_with_no_args(self):
        """checking BaseModel when instiantied with no arguments"""
        bm = BaseModel()
        self.assertIsNotNone(bm.id)
        self.assertIsInstance(bm.created_at, dt.datetime)
        self.assertIsInstance(bm.updated_at, dt.datetime)
        self.assertEqual(bm.created_at, bm.updated_at)
        self.assertIn(bm, storage.all().values())

    def test_init_with_kwargs(self):
        """checking BaseModel when instantiated with arguments"""
        created_at = datetime.datetime(2023, 9, 8)
        updated_at = datetime.datetime(2023, 9, 9)
        bm = BaseModel(id="123", created_at=created_at.isoformat(), updated_at=updated_at.isoformat())
        self.assertEqual(bm.id, "123")
        self.assertEqual(bm.created_at, created_at)
        self.assertEqual(bm.updated_at, updated_at)

    def test_str_representation(self):
        """"checks the string representation __str__ of BaseModel"""
        bm = BaseModel()
        bm.id = "test_id"
        bm.created_at = datetime.datetime(2023, 9, 8)
        bm. updated_at = datetime.datetime(2023, 8, 9)
        expected_str = "[BaseModel] (test_id) {'id': 'test_id', 'created_at': '2023-09-08 00:00:00', 'updated_at': '2023-09-09 00:00:00'}"
        self.assertEqual(str(bm), expected_str)

    def test_save_method(self):
        """checking the behaviour of the save_method of the BaseModel class"""
        bm = BaseModel()
        previous_updated_at = bm.updated_at
        bm.save()
        self.assertGreater(bm.updated_at, previous_updated_at) # verifies that the updated_at attribute has been updated and is greater than its previous value.

    def test_to_dict_method(self):
        """"checks the behaviour of the to_dict method of the BaseModel"""
        bm = BaseModel() # instance of BaseModel
        bm_dict = bm.to_dict() # to_dict method is called on the instance, producing a dictionary
        self.assertIsInstance(bm_dict, dict) # to verify that the result is a dictionary
        self.assertEqual(bm_dict['__class__'], 'BaseModel') # checks if the 'class' attribute is correctly included
        self.assertIn('id', bm_dict)
        self.assertIn('created_at', bm_dict)
        self.assertIn('updated_at', bm_dict)



if __name__ == '__main__':
    unittest.main()
