#!/usr/bin/python3
"""Test for Amenity"""
import unittest
from datetime import datetime
import uuid
from time import sleep
import sys
# sys.path.append('../..')
from models.base_model import BaseModel
from models.amenity import Amenity


class test_Amenity(unittest.TestCase):

    def test_amenity_type(self):
        amenity = Amenity()
        self.assertEqual(type(amenity), Amenity)

    def test_city_as_a_subclas(self):
        amenity = Amenity()
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_state_name(self):
        self.assertEqual(type(Amenity.name), str)


if __name__ == '__main__':
    unittest.main()
