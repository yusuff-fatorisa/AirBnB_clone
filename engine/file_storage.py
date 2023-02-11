#!/usr/bin/python3
"""
This module contains a class 'FileStorage' that
serializes instances to a JSON file and
deserializes JSON file to instances
"""


class FileStorage(object):
    """
    This class serializes an instance of the class to
    JSON file and deserializes a file to an instances.

    ==== Private Attributes ====

    __file_path: this is a string, that serves as a path
    to the JSON file

    __objects: This is a dictionary, which is empty, but
    will store all objects by the class id

    =====  Public Methods  =====

    all(self): It returns the dictionary '__objects'

    new(self, obj): It sets inside '__objects', the 'obj'
    with the key 'obj class name'.id

    save(self): serializes the JSON file to '__objects': __filepath

    reload(self): deserializes the JSON file to "__objects" if __filepath
    exists, else does nothing with no exception raised
    """
