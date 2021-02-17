#!/usr/bin/python3
"""SIRNIKOLAX raja de aca"""
import json
import os
import datetime


class FileStorage:
    """
    Serializes instances to a JSON file and
    deserializes Json file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Initializes instance"""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        # obj.__dict__["updated_at"] = str(obj.__dict__["created_at"])
        # obj.__dict__["created_at"] = str(obj.__dict__["created_at"])
        self.__objects[str(obj.__class__.__name__) +
                       "." + obj.id] = obj.__dict__

    def save(self):
        """Serializes __objects to the JSON file"""
        if self.__objects:
            for key25, value25 in self.__objects.items():
                newdict = value25.copy()
                for key225, value225 in newdict.items():
                    if not value225:
                        del value25[key225]
                self.__objects[key25] = value25
            for key, values in self.__objects.items():
                for key2, value2 in values.items():
                    if key2 == "created_at":
                        values[key2] = str(value2)
                    elif key2 == "updated_at":
                        values[key2] = str(value2)
            with open(self.__file_path, mode='w') as my_file:
                json.dump(self.__objects, my_file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as my_file:
                one_obj_dictionary = json.load(my_file)
                for key, value in one_obj_dictionary.items():
                    self.__objects[key] = value
        else:
            return

