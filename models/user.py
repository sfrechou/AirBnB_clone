#!/usr/bin/python3
""" User module """
from models.base_model import BaseModel


class User(BaseModel):
    """ Create User """

    def __init__(self):
        """ Initializes instance """
        super().__init__()
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

