#!/usr/bin/python3
import uuid
import datetime as dt

class BaseModel:
        def __init__(self) -> None:
                """this is the constructur function"""
                self.id = str(uuid.uuid4())
                self.created_at = dt.datetime.now()
                self.updated_at = self.created_at
        
        def __str__(self):
                """the string representation of the class"""
                return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

        def save(self):
                """updates the updated_at attribute of the class"""
                self.updated_at = dt.datetime.now()
        
        def to_dict(self):
                """creates a dictionary conating all keys and class names and returns it"""
                dictionary = self.__dict__.copy()
                dictionary['__class__'] = type(self).__name__
                dictionary['created_at'] = self.created_at.isoformat()
                dictionary['updated_at'] = self.updated_at.isoformat()
                return dictionary
                
