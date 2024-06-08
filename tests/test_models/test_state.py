#!/usr/bin/python3
"""Test for State"""
import unittest
from datetime import datetime
import uuid
from time import sleep
import sys
sys.path.append('../..')
from models.base_model import BaseModel
from models.state import State


class test_State(unittest.TestCase):

    def test_city_type(self):
        state = State()
        self.assertEqual(type(state), State)

    def test_city_as_a_subclas(self):
        state = State()
        self.assertTrue(issubclass(State, BaseModel))

    def test_state_name(self):
        self.assertEqual(type(State.name), str)


if __name__ == '__main__':
    unittest.main()
