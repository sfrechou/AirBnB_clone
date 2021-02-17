#!/usr/bin/python3
"""raja de aca"""
import uuid
import datetime
import csv
from models import storage
 
 
class BaseModel:
    """Defines all common attributes/methods for other classes"""
 
    def __init__(self, *args, **kwargs):
        """Initializes object"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at":
                        value = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    if key == "updated_at":
                        value = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)
 
    def __str__(self):
        """Returns string representation"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))
 
    def save(self):
        """Updates the public instance attr with current datetime"""
        self.updated_at = datetime.datetime.now()
        storage.save()
 
    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__"""
        self.__dict__["__class__"] = self.__class__.__name__
        self.__dict__["created_at"] = self.created_at.isoformat()
        self.__dict__["updated_at"] = self.updated_at.isoformat()
        return self.__dict__
 

