#!/usr/bin/python3
"""
the user model
"""
from models.base_model import BaseModel

class User(BaseModel):
        """the user class"""
        def __init__(self, *args, **kwargs) -> None:
                super().__init__(*args, **kwargs)
                self.email = ''
                self.password = ''
                self.first_name = ''
                self.last_name = ''
        