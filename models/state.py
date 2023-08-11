#!/usr/bin/python3
""""This is the state model"""
from models.base_model import BaseModel

class State(BaseModel):
    """This is a State class that inherits from BaseModel.

    Attribute:
        name(str): The name of the state
    """
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.name = ""
