#!/usr/bin/python3
"""
module conatining the class review,
it inherite from BaseModel class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    state class
    """
    place_id = ""
    user_id = ""
    text = ""
