#!/usr/bin/python3
"""The BaseModel class that defines all common attributes and methods"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """The base model class"""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of BaseModel

        Args:
            *args: Unused.
            **kwargs: Key-value pairs of attributes.
        """
        date_format = "%Y-%m-%dT%H:%M:%S.%f"

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    setattr(self, key, datetime.strptime(value, date_format))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """Return the string representation of the BaseModel instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the updated_at attribute and save the model to storage"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Create a dictionary representation of the instance

        Returns:
            dict: Dictionary containing all instance attributes.
        """
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
