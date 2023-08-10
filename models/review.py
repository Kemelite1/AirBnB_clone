#!/usr/bin/python3
""""This is the Review model"""
from models.base_model import BaseModel

class Review(BaseModel):
    """This is a Review class that inherits from BaseModel"""
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.tetx = ""
