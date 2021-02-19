#!/usr/bin/python3
"""raja de aca"""
import json
import os
import datetime
from models.base_model import BaseModel

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
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        ser_dict = {}
        all_dict = FileStorage.__objects
        with open(FileStorage.__file_path, 'w') as my_file:
            for value in all_dict.values():
                ser_dict["{}.{}".format(value.__class__.__name__, value.id)] = value.to_dict()
            json.dump(ser_dict, my_file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as my_file:
                one_obj_dictionary = json.load(my_file)
                for key, value in one_obj_dictionary.items():
                    final_key = key.split('.')
                    class_name = final_key[0]
                    self.new(eval("{}".format(class_name))(**value))
