#!/usr/bin/python3
"""
This module contains a 'User' class
that inherits from BaseModel class
"""

from base_model import BaseModel


class User(BaseModel):
    """
    This class inherits from the BaseModel class

    =====  Public Class Attributes  =====
    email => string - empty string
    password => string - empty string
    first_name => string - empty string
    last_name => string - empty string

    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
