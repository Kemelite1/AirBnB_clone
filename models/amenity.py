#!/usr/bin/python3
""""This is the amenity model"""
from models.base_model import BaseModel

class Amenity(BaseModel):
    """This is Amenity class that inherits from BaseModel"""
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.name = ""
