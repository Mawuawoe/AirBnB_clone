#!/usr/bin/python3
"""
module conatining the class user,
it inherite from BaseModel class
"""

import json
import os
from models.base_model import BaseModel


class User(BaseModel):
    """
    class User, it handles user data
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
