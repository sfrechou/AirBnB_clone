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
                    formatx = "%Y-%m-%dT%H:%M:%S.%f"
                    if key == "created_at":
                        self.__dict__[key] = datetime.datetime.\
                                             strptime(value, formatx)
                    if key == "updated_at":
                        self.__dict__[key] = datetime.datetime.\
                                             strptime(value, formatx)
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
        new_time = datetime.datetime.now()
        self.updated_at = new_time
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__"""
        dict_returned = {}
        for key, value in self.__dict__.items():
            dict_returned[key] = value
        dict_returned["__class__"] = self.__class__.__name__
        dict_returned["created_at"] = self.created_at.isoformat()
        dict_returned["updated_at"] = self.updated_at.isoformat()
        return (dict_returned)
