#!/usr/bin/python3
""""This is the Review model"""
from models.base_model import BaseModel

class Review(BaseModel):
    """This is a Review class that inherits from BaseModel"""
    place_id = ""
    user_id = ""
    tetx = ""
