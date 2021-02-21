#!/usr/bin/python3
"""File storage class"""
import json
import os
import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Serializes instances to a JSON file and
    deserializes Json file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        # obj.__dict__["updated_at"] = str(obj.__dict__["created_at"])
        # obj.__dict__["created_at"] = str(obj.__dict__["created_at"])
        self.__objects[str(obj.__class__.__name__) +
                       "." + str(obj.id)] = obj

    def save(self):
        """serializes __objects to a JSON path from __file_path
        """
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()

        with open(self.__file_path, 'w') as filee:
            json.dump(new_dict, filee)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as my_file:
                one_obj_dictionary = json.load(my_file)
                for key, value in one_obj_dictionary.items():
                    key_name = key.split('.')
                    name_class = key_name[0]
                    self.new(eval("{}".format(name_class))(**value))
        else:
            return
