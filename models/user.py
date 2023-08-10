#!/usr/bin/python3
"""
the user model
"""
from models.base_model import BaseModel

class User(BaseModel):
        """the User class.

        Attributes of User class:

            email(str): User's email.

            password(str): User's password.

            first_name(str): User's first name

            last_name(str): User's last name.
        """
        def __init__(self, *args, **kwargs) -> None:
                super().__init__(*args, **kwargs)
                self.email = ''
                self.password = ''
                self.first_name = ''
                self.last_name = ''
        
