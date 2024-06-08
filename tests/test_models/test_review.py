#!/usr/bin/python3
"""Test for Review"""
import unittest
from datetime import datetime
import uuid
from time import sleep
import sys
# sys.path.append('../..')
from models.base_model import BaseModel
from models.review import Review


class test_Review(unittest.TestCase):

    def test_review_type(self):
        rview = Review()
        self.assertEqual(type(rview), Review)

    def test_review_as_a_subclas(self):
        rview = Review()
        self.assertTrue(issubclass(Review, BaseModel))

    def test_review_place_id(self):
        self.assertEqual(type(Review.place_id), str)

    def test_review_user_id(self):
        self.assertEqual(type(Review.user_id), str)

    def test_review_text(self):
        self.assertEqual(type(Review.text), str)


if __name__ == '__main__':
    unittest.main()
