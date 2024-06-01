#!/usr/bin/python3
"""Module containing a class that handles storing objects in a file"""

from models.base_model import BaseModel
import json
import os


class FileStorage:
    """Class that serializes instances to
    a JSON file and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id"""
        obj_class_name = obj.__class__.__name__
        FileStorage.__objects[f"{obj_class_name}.{obj.id}"] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)"""
        objdict2 = {key: obj.to_dict() \
                    for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as fp:
            json.dump(objdict2, fp)

    def reload(self):
        """Deserialize the JSON file to __objects, if it exists"""
        if os.path.exists(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path) as fp_2:
                    objdict = json.load(fp_2)
                    for o in objdict.values():
                        cls_name = o["__class__"]
                        del o["__class__"]
                        self.new(eval(cls_name)(**o))
            except FileNotFoundError:
                pass
