#!/usr/bin/python3
"""unittest for the BaseModel class"""

import unittest
from datetime import datetime
from models import storage
from models.base_model import BaseModel
import pycodestyle


class TestBaseModel(unittest.TestCase):
    """unittests to test the for the BaseModel class"""

    def test_pepcodestyle(self):
        """test pepcodestyle"""
        for path in ['models/base_model.py',
                     'tests/test_models/test_base_model.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_init(self):
        """checking BaseModel when instiantied with no arguments"""
        bm = BaseModel()
        bm1 = BaseModel()
        self.assertIsInstance(bm, BaseModel)
        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)
        self.assertEqual(bm.created_at, bm.updated_at)
        self.assertIn(bm, storage.all().values())
        self.assertNotEqual(bm.id, bm1.id)

    def test_str(self):
        """test that the str method has the correct output"""
        inst = BaseModel()
        string = "[BaseModel] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(string, str(inst))

    def test_save(self):
        """checking the behaviour of the save_method of the BaseModel class"""
        bm = BaseModel()
        up_old = bm.updated_at
        cr_old = bm.created_at
        bm.save()
        up_new = bm.updated_at
        cr_new = bm.created_at
        self.assertEqual(up_old, cr_old)
        self.assertEqual(up_new, cr_new)

    def test_to_dict(self):
        """"checks the behaviour of the to_dict method of the BaseModel"""
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertIsInstance(bm_dict, dict)
        self.assertEqual(bm_dict['__class__'], 'BaseModel')
        self.assertIn('id', bm_dict)
        self.assertIn('created_at', bm_dict)
        self.assertIn('updated_at', bm_dict)

        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.assertEqual(bm_dict["__class__"], "BaseModel")
        self.assertEqual(type(bm_dict["created_at"]), str)
        self.assertEqual(type(bm_dict["updated_at"]), str)
        self.assertEqual(bm_dict["created_at"],
                         bm.created_at.strftime(t_format))
        self.assertEqual(bm_dict["updated_at"],
                         bm.updated_at.strftime(t_format))


if __name__ == '__main__':
    unittest.main()
