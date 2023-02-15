#!/usr/bin/python3
"""
This module contains a class that
inherits from 'BaseModel'
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    This class inherits from BaseModel

    ===== Public Class Attributes  ======
    name => string - empty string
    """

    name = ""
