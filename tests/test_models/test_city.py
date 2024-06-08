#!/usr/bin/python3
"""Test for city"""
import unittest
from datetime import datetime
import uuid
from time import sleep
import sys
# sys.path.append('../..')
from models.base_model import BaseModel
from models.city import City


class test_City(unittest.TestCase):

    def test_city_type(self):
        city = City()
        self.assertEqual(type(city), City)

    def test_city_as_a_subclas(self):
        city = City()
        self.assertTrue(issubclass(City, BaseModel))

    def test_city_state_id(self):
        self.assertEqual(type(City.state_id), str)

    def test_city_name(self):
        self.assertEqual(type(City.name), str)


if __name__ == '__main__':
    unittest.main()
