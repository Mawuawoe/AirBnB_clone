#!/usr/bin/python3
"""Test for file storage"""
import unittest
from datetime import datetime
import uuid
from time import sleep
import sys
sys.path.append('../../..')
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json
import os
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class test_File_Storage(unittest.TestCase):
    """
    Test for the class file_storage
    """

    def test_file_storage_type(self):
        storage = FileStorage()
        self.assertEqual(type(storage), FileStorage)

    def test__file_path_type(self):
        storage = FileStorage()
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test__objects_type(self):
        storage = FileStorage()
        self.assertEqual(type(storage._FileStorage__objects), dict)

    def test_all(self):
        storage = FileStorage()
        objects = storage.all()
        self.assertEqual(type(objects), dict)

    def test_new(self):
        bm = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        ame = Amenity()
        rview = Review()
        storage = FileStorage()
        storage.new(bm)
        storage.new(user)
        storage.new(state)
        storage.new(place)
        storage.new(city)
        storage.new(ame)
        storage.new(rview)
        self.assertIn("BaseModel." + bm.id, storage.all().keys())
        self.assertIn("User." + user.id, storage.all().keys())
        self.assertIn("State." + state.id, storage.all().keys())
        self.assertIn("Place." + place.id, storage.all().keys())
        self.assertIn("City." + city.id, storage.all().keys())
        self.assertIn("Amenity." + ame.id, storage.all().keys())
        self.assertIn("Review." + rview.id, storage.all().keys())

    def test_save(self):
        bm = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        ame = Amenity()
        rview = Review()
        storage = FileStorage()
        storage.new(bm)
        storage.new(user)
        storage.new(state)
        storage.new(place)
        storage.new(city)
        storage.new(ame)
        storage.new(rview)
        storage.save()
        file_content = ""
        with open("file.json", 'r') as fp:
            file_content = fp.read()
            self.assertIn("BaseModel." + bm.id, file_content)
            self.assertIn("User." + user.id, file_content)
            self.assertIn("State." + state.id, file_content)
            self.assertIn("Place." + place.id, file_content)
            self.assertIn("City." + city.id, file_content)
            self.assertIn("Amenity." + ame.id, file_content)
            self.assertIn("Review." + rview.id, file_content)

    def test_reload(self):
        bm = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        ame = Amenity()
        rview = Review()
        storage = FileStorage()
        storage.new(bm)
        storage.new(user)
        storage.new(state)
        storage.new(place)
        storage.new(city)
        storage.new(ame)
        storage.new(rview)
        storage.save()
        storage.reload()
        objs = storage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objs)
        self.assertIn("User." + user.id, objs)
        self.assertIn("State." + state.id, objs)
        self.assertIn("Place." + place.id, objs)
        self.assertIn("City." + city.id, objs)
        self.assertIn("Amenity." + ame.id, objs)
        self.assertIn("Review." + rview.id, objs)


if __name__ == '__main__':
    unittest.main()
