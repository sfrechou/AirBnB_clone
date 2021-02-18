#!/usr/bin/python3
"""raja de aca"""
import json
import os
import datetime
import ast
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

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
                       "." + obj.id] = obj.__dict__

    def save(self):
        """Serializes __objects to the JSON file"""
        new_dict = {}
        for key, value in self.__objects.items():
            class_name = key.split(".")
            if type(value) == str:
                list_val = value.split()
                del list_val[:2]
                new_str = ""
                for ele in list_val:
                    new_str += ele
            else:
                value["__class__"] = class_name[0]
                new_dict[key] = str(value)

        with open(FileStorage.__file_path, "w") as my_file:
            json.dump(new_dict, my_file)
        
        for key, value in self.__objects.items():
            if type(value) == dict:
                del value["__class__"]
        

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as my_file:
                one_obj_dictionary = json.load(my_file)
                for i, j in one_obj_dictionary.items():
                    k = eval(j)
                    del k["__class__"]
                    j = str(k)
                    new_id = i.split(".")
                    new = "[" + new_id[0] + "] (" + new_id[1] + ")"
                    self.__objects[i] = new + " " + j
                    # self.new(eval(new_id[0])(**k))
        else:
            return
