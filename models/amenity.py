#!/usr/bin/python3
from models.base_model import BaseModel
""""
This is the amenity model
"""


class Amenity(BaseModel):
    """This is Amenity class that inherits from BaseModel"""
    
    def __init__(self, *args, **kwargs) -> None:
        """Constructor"""
        super().__init__(*args, **kwargs)
        self.name = ""
