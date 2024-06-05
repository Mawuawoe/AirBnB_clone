#!/usr/bin/python3
"""
module conatining the class city,
it inherite from BaseModel class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    state class
    """
    state_id = ""
    name = ""
