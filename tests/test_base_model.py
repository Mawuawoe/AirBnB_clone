#!/usr/bin/python3
"""Test for base model"""
import unittest
from time import sleep
import sys
sys.path.append('..')
import datetime
import uuid
from models.base_model import BaseModel


class test_BaseModel(unittest.TestCase):
    """testing the basemodel"""

    def setUp(self):
        self.my_model = BaseModel()
        sleep(0.05)
        self.my_model_2 = BaseModel()

    def tearDown(self):
        del self.my_model

    def test_isbasemodelclass (self):
        self.assertEqual(type(self.my_model), BaseModel)

    def test_id(self):
        self.assertEqual(type(self.my_model.id), str)
    
    def test_created_at(self):
        self.assertEqual(type(self.my_model.created_at), datetime.datetime)

    def test_updated_at(self):
        self.assertEqual(type(self.my_model.updated_at), datetime.datetime)
    
    def test_unique_ids(self):
        self.assertNotEqual(self.my_model_2.id, self.my_model.id)
    
    def test_2_models_diff_in_craeted_at(self):
        self.assertLess(self.my_model.created_at, self.my_model_2.created_at)

    def test_2_models_diff_in_updated_at(self):
        self.assertLess(self.my_model.updated_at, self.my_model_2.updated_at)

if __name__ == '__main__':
    unittest.main()
