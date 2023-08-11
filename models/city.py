#!/usr/bin/python3
""""This is the city model"""
from models.base_model import BaseModel

class City(BaseModel):
    """This is a City class that inherits from BaseModel"""
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
