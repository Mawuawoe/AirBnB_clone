#!/usr/bin/python3
""" The base_model class that define all common attributes and methods"""
import uuid
from datetime import datetime


class BaseModel():
    """ the base model class"""

    def __init__(self):
        self.id = str((uuid.uuid4()))
        """unique identifier"""
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """the string rep of basemodel"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        self.updated_at = datetime.today()

    def to_dict(self):
        """creating a new dict of instance atributes"""
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
