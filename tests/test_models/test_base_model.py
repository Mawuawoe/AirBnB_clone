#!/usr/bin/python3
"""Test for base model"""
import unittest
from datetime import datetime
import uuid
from time import sleep
import sys
# sys.path.append('../..')
from models.base_model import BaseModel


class test_BaseModel(unittest.TestCase):
    """testing the basemodel"""

    def setUp(self):
        self.my_model = BaseModel()
        sleep(0.05)
        self.my_model_2 = BaseModel()
        dict = {'id': '1234',
                'created_at': '2017-09-28T21:05:54.119427',
                'updated_at': '2017-09-28T21:05:56.119427'}
        self.new_model = BaseModel(**dict)

    def tearDown(self):
        del self.my_model
        del self.my_model_2
        del self.new_model

    def test_isbasemodelclass(self):
        self.assertEqual(type(self.my_model), BaseModel)

    def test_id(self):
        self.assertEqual(type(self.my_model.id), str)

    def test_created_at(self):
        self.assertEqual(type(self.my_model.created_at), datetime)

    def test_updated_at(self):
        self.assertEqual(type(self.my_model.updated_at), datetime)

    def test_unique_ids(self):
        self.assertNotEqual(self.my_model_2.id, self.my_model.id)

    def test_2_models_diff_in_craeted_at(self):
        self.assertLess(self.my_model.created_at, self.my_model_2.created_at)

    def test_2_models_diff_in_updated_at(self):
        self.assertLess(self.my_model.updated_at, self.my_model_2.updated_at)

    def test_str_rep(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.id = "12345"
        bm.created_at = bm.updated_at = dt
        bmstr = bm.__str__()
        self.assertIn("[BaseModel] (12345)", bmstr)
        self.assertIn("'created_at': " + dt_repr, bmstr)
        self.assertIn("'updated_at': " + dt_repr, bmstr)
        self.assertIn("'id': '12345'", bmstr)

    def test_kwargs_id(self):
        self.assertEqual(self.new_model.id, '1234')

    def test_kwargs_created_at(self):
        self.assertEqual(type(self.new_model.created_at), datetime)

    def test_kwargs_updated_at(self):
        self.assertEqual(type(self.new_model.updated_at), datetime)

    def test_str_rep(self):
        my_dict = {'id': '1234',
                   'created_at': '2017-09-28T21:05:54.119427',
                   'updated_at': '2017-09-28T21:05:56.119427'}
        bm2 = BaseModel(**my_dict)
        bmstr2 = bm2.__str__()
        self.assertIn("[BaseModel] (1234)", bmstr2)
        self.assertIn("'created_at':\
 datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)",
                      bmstr2)
        self.assertIn("'updated_at':\
 datetime.datetime(2017, 9, 28, 21, 5, 56, 119427)",
                      bmstr2)
        self.assertIn("'id': '1234'", bmstr2)

    def test_save(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)

    def test_to_dict_type(self):
        bm = BaseModel()
        self.assertTrue(dict, type(bm.to_dict()))

    def test_to_dict_keys(self):
        bm = BaseModel()
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())

    def test_to_dict_output(self):
        dt = datetime.today()
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        to_dict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(bm.to_dict(), to_dict)


if __name__ == '__main__':
    unittest.main()
