#!/usr/bin/python3
"""
This module contains a class 'BaseModel'
which defines all common attributes/methods
for other classes.
"""

import uuid
from datetime import datetime as dt
from models import storage


class BaseModel(object):
    """
    This class deines all commom attributes
    or methods for other classes

    Attributes includes
    id => a string assigned with an uuid for an instance
    created_at => the datetime when an instance was created
    updated_at => the datetime when an instance is crerated / modified
    """
    def __init__(self, *args, **kwargs):
        """
         Instantiates the base_model object
        """
        self.id = str(uuid.uuid4())
        self.created_at = dt.now()
        self.updated_at = dt.now()
        if kwargs:
            for key, val in kwargs.items():
                if key in ["created_at, updated_at"]:
                    val = dt.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                elif key != "__class__":
                    setattr(self, key, val)
                else:
                    pass

    def __str__(self):
        """ prints a representation of the object """
        return f"{[self.__class__.__name__]} {(self.id)} {self.__dict__}"

    def save(self):
        """updates the public instance attribute
           'updated_at' with the current datetime.
        """
        self.updated_at = dt.now()
        storage.save(self)

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of
        '__dict__' of the instance or object.
        """
        fmt = "%Y-%m-%dT%H:%M:%S.%f"
        self.__dict__["__class__"] = self.__class__.__name__
        self.__dict__["created_at"] = self.created_at.strftime(fmt)
        self.__dict__["updated_at"] = self.updated_at.strftime(fmt)
        return self.__dict__
