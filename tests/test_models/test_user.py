#!/usr/bin/python3
"""Test for user"""
import unittest
from datetime import datetime
import uuid
from time import sleep
import sys
# sys.path.append('../..')
from models.base_model import BaseModel
from models.user import User


class test_User(unittest.TestCase):

    def test_user_type(self):
        user = User()
        self.assertEqual(type(user), User)

    def test_user_as_a_subclas(self):
        user = User()
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_email(self):
        self.assertEqual(type(User.email), str)

    def test_user_password(self):
        self.assertEqual(type(User.password), str)

    def test_user_first_name(self):
        self.assertEqual(type(User.first_name), str)

    def test_user_last_name(self):
        self.assertEqual(type(User.last_name), str)


if __name__ == '__main__':
    unittest.main()
