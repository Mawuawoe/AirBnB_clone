#!/usr/bin/python3
"""Test for Place"""
import unittest
from datetime import datetime
import uuid
from time import sleep
import sys
sys.path.append('../..')
from models.base_model import BaseModel
from models.place import Place


class test_Place(unittest.TestCase):

    def test_place_type(self):
        place = Place()
        self.assertEqual(type(place), Place)

    def test_place_as_a_subclas(self):
        place = Place()
        self.assertTrue(issubclass(Place, BaseModel))

    def test_place_city_id(self):
        self.assertEqual(type(Place.city_id), str)

    def test_place_user_id(self):
        self.assertEqual(type(Place.user_id), str)

    def test_place_name(self):
        self.assertEqual(type(Place.name), str)

    def test_place_description(self):
        self.assertEqual(type(Place.description), str)

    def test_place_number_rooms(self):
        self.assertEqual(type(Place.number_rooms), int)

    def test_place_number_bathroom(self):
        self.assertEqual(type(Place.number_bathrooms), int)

    def test_place_max_guest(self):
        self.assertEqual(type(Place.max_guest), int)

    def test_place_price_by_night(self):
        self.assertEqual(type(Place.price_by_night), int)

    def test_latitude(self):
        self.assertEqual(type(Place.latitude), float)

    def test_longitude(self):
        self.assertEqual(type(Place.longitude), float)

    def test_amenity_ids(self):
        self.assertEqual(type(Place.amenity_ids), list)


if __name__ == '__main__':
    unittest.main()
