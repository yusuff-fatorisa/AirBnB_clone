#!/usr/bin/python3
"""
This module contains a class 'FileStorage' that
serializes instances to a JSON file and
deserializes JSON file to instances
"""

import json
from os.path import exists


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

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary '__objects' """
        return FileStorage.__objects

    def new(self, obj):
        """ sets inside '__objects' the 'obj' with 'obj class name'.id """
        print("New Created Instance ID ==> {}".format(obj.id))
        FileStorage.__objects[obj.id] = obj
        print("====== ======== ========= ======== ===========")
        print(FileStorage.__objects)

    def save(self):
        """ serializes '__objects' to JSON file using __file_path """
        with open(FileStorage.__file_path, "a", encoding="utf-8") as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """ deserializes the JSON file to '__objects' only if it exist """
        try:
            if exists(FileStorage.__file_path):
                with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                    FileStorage.__objects = json.load(f)
        except json.decoder.JSONDecodeError:
            pass
