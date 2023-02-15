#1/usr/bin/python3
"""
This module contains a class that inherits
from BaseModel
"""

from base_model import BaseModel


class Review(BaseModel):
    """
    This class inherits from BaseModel

    =====  Public Class Attributes =====
    place_id => string empty string
    user_id => string - empty string
    text => string - empty string
    """

    place_id = ""
    user_id = ""
    text = ""
