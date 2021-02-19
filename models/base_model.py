#!/usr/bin/python3
"""Module for BaseModel Class"""
import uuid
from datetime import datetime
import csv
import models


class BaseModel:
    """ class for all other classes to inherit from """

    def __init__(self, *args, **kwargs):
        """ Constructor and re-create an instance with
        this dictionary representation"""
        formatx = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "updated_at":
                    value = datetime.strptime(value, formatx)
                elif key == "created_at":
                    value = datetime.strptime(value, formatx)
                elif key == "__class__":
                    continue

                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns string representation"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """Updates the public instance attr with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__"""
        new_dict = dict(self.__dict__)
        new_dict["__class__"] = self.__class__.__name__
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["created_at"] = self.created_at.isoformat()
        return new_dict
