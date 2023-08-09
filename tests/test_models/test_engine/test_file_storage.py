#!/usr/bin/python3
"""unittest for the FileStorage class"""

import unittest
import models
import os
import json
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """"test cases for the FileStorage class"""

    def setUp(self):
        """sets up test methods"""
        pass

    def tearDown(self):
        """tear down test methods"""
        self.reset_storage()

    def reset_storage(self):
        """Reset FileStorage data"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage__file_path):
            os.remove(FileStorage.FileStorage__file_path)

    def test_file_storage_instantiation(self):
        """Test instantiation of the FileStorage class"""
        storage = FileStorage()
        self.assertEqual(type(storage).__name__, "FileStorage")

    def test_new_method(self):
        """testing the new() method of FileStorage"""
        storage = FileStorage()
        instance = FileStorage()
        instance.id = "test_id"
        instance.key = "value"
        storage.new(instance)
        self.assertTrue("FileStorage.test_id" in storage.all())
        self.assertEqual(storage.all()["FileStorage.test_id"], instance)

    def test_save_method(self):
        """testing the save() method of FileStorage"""
        storage = FileStorage()
        instance = FileStorage()
        instance.id = "test_id"
        instance.key = "value"
        storage.new(instance)

        with open('file.json', 'w') as f:
            f.write("") #empty file for testing

        storage.save()

        with open('file.json', 'r') as f:
            data = json.load(f)
            self.assertIn("FileStorage.test_id", data)
            self.assertEqual(data["FileStorage.test_id"]["id"], "test_id")
            self.assertEqual(data["FileStorage.test_id"]["key"], "value")

    def test_reload_method(self):
        """"testing the reload() method of FileStorage"""
        instance_data = '{"FileStorage.test_id": {"id": "test_id", "key": "value"}}'
        with open('file.json', 'w') as f:
            f.write(instance_data)  # Write instance data to the file

        storage = FileStorage()
        storage.reload()
        self.assertIn("FileStorage.test_id", storage.all())
        instance = storage.all()["FileStorage.test_id"]
        self.assertEqual(instance.__class__.__name__, "FileStorage")
        self.assertEqual(instance.id, "test_id")
        self.assertEqual(instance.key, "value")

    def test_classes_method(self):
        """testing the classes() method of FileStoraage"""
        storage = FileStorage()
        classes_method = storage.classes()
        self.assertEqual(classes_method.__name__, "BaseModel")


if __name__ == '__main__':
    unittest.main()
