#!/usr/bin/python3
"""raja de aca"""
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
        # obj.__dict__["created_at"] = str(obj.__dict__["created_at"]
        self.__objects[str(obj.__class__.__name__) +
                       "." + obj.id] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        dict_of_dicts = {}
        for key, value in self.__objects.items():
            dict_of_dicts[key] = value.to_dict()

        with open(FileStorage.__file_path, "w") as my_file:
            json.dump(dict_of_dicts, my_file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as my_file:
                one_obj_dictionary = json.load(my_file)

                for key, value in one_obj_dictionary.items():
                    self.__objects[key] = value
        else:
            return
