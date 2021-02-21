#!/usr/bin/python3
"""Base model class"""
import uuid
from datetime import datetime
import csv
import models


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes object"""
        now = str(datetime.now())
        now = datetime.strptime(now, "%Y-%m-%d %H:%M:%S.%f")
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at":
                        value = now
                    if key == "updated_at":
                        value = now
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
        dict_returned = dict(self.__dict__)
        dict_returned["created_at"] = self.created_at.isoformat()
        dict_returned["updated_at"] = self.updated_at.isoformat()
        dict_returned["__class__"] = self.__class__.__name__
        return dict_returned