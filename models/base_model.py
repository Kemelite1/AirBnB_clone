#!/usr/bin/python3
"""
base_model module
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """base model class"""

    def __init__(self, *args, **kwargs) -> None:
        """this is the constructur function"""
        if kwargs:
            for key, val in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    new_val = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                    new_val.isoformat()
                    setattr(self, key, new_val)
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """the string representation of the class"""
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the updated_at attribute of the class"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
            creates a dictionary conating all keys
            and class names and returns it
        """
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = type(self).__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
