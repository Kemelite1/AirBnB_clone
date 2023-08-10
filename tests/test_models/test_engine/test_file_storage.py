#!/usr/bin/python3
"""unittest for the FileStorage class"""

import unittest
import os
import json
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import pycodestyle

class TestFileStorage(unittest.TestCase):
    """"test cases for the FileStorage class"""

    def test_pepcodestyle(self):
        """test pepcodestyle"""
        for path in ['models/base_model.py',
                     'tests/test_models/test_base_model.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_all(self):
        """test all method"""
        stored = FileStorage()
        self.assertIsInstance(stored.all(), dict)
        

    def test_init(self):
        """Test instantiation of the FileStorage class"""
        storage = FileStorage()
        self.assertEqual(type(storage).__name__, "FileStorage")

    def test_new(self):
        """testing the new() method of FileStorage"""
        stored = FileStorage()
        bm = BaseModel()
        stored.new(bm)
        st = list(stored.all().values())
        for l in st:
            if l.id == bm.id:
                self.assertEqual(l, bm)

    def test_save_and_reload(self):
        """testing the save() method of FileStorage"""
        stored = FileStorage()
        bm = BaseModel()
        stored.new(bm)
        stored.save()
        stored.reload()
        
        st = stored.all()
        self.assertIn("{}".format(type(bm).__name__ + '.'+ bm.id), st)


if __name__ == '__main__':
    unittest.main()
