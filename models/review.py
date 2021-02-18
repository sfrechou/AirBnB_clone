#!/usr/bin/python3
""" User module """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review of the AirBnB """
    place_id = ""
    user_id = ""
    text = ""
