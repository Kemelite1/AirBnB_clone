#!/usr/bin/python3
"""unittest for the BaseModel class"""

import unittest
import models
import os
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel_instantiation(unittest.TestCase):
    """unittests to test the instantiation of the BaseModel class"""

    def test_no_args_instantiates(self):
        """"tests if a BaseModel instance is created when no arguments are provided and checks if the type is BaseModel"""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        """checks if a newly created BaseModel instance is stored in models.storage dictionary"""
        self.assertEqual(BaseModel(), models.storage.all().values())

    def test_id_is_public_str(self):
        """checks that the id attribute of the BaseModel instance is a string"""
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        """to verify that the created_at attribute is a datetime object"""
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        """"to verify that the updated_at attribute of BaseModel instance is a datetime object"""

    def test_two_models_unique_ids(self):
        """checks if two BaseModel instances created id attributes are unique"""
        base_model_1 = BaseModel()
        base_model_2 = BaseModel()
        self.assertNotEqual(base_model_1.id, base_model_2.id)

    def test_two_models_different_created_at(self):
        """"checks that the created_at attribute for two BaseModel instances are not the same"""
         base_model_1 = BaseModel()
         base_model_2 = BaseModel()
         self.assertNotEqual(base_model_1.created_at, base_model_2.created_at)

    def test_two_models_different_updated_at(self):
        """checks that the updated_at attribute for two BaseModel instances are not the same"""
        base_model_1 = BaseModel()
        base_model_2 = BaseModel()
        self.assertNotEqual(base_model_1.updated_at, base_model_2.updated_at)

    def test_str_representation(self):
        """checks to see if an instance's __str__ representation contains expected information"""



if __name__ == '__main__':
    unittest.main()
