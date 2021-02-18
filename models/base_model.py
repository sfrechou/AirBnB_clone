#!/usr/bin/python3
"""raja de aca"""
import uuid
from datetime import datetime
import csv
from models import storage


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
            storage.new(self)
 
    def __str__(self):
        """Returns string representation"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))
 
    def save(self):
        """Updates the public instance attr with current datetime"""
        self.updated_at = datetime.now()
        storage.save()
 
    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__"""
        dict_returned = {}
        dict_returned["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                formatx = "%Y-%m-%dT%H:%M:%S.%f"
                dict_returned[key] = value.strftime(formatx)
            else:
                dict_returned[key] = value
        return (dict_returned)
