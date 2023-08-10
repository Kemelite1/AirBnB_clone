#!/usr/bin/python3
"""
file storage module
"""
import json
import os


class FileStorage:
    """CLASS"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """return the file path"""
        return self.__objects

    def new(self, obj):
        """add a new object to the __object attribute"""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """save the objects to a json file"""
        with open(self.__file_path , "w") as f:
            stored = {key: val.to_dict() for key, val in self.__objects.items()}
            json.dump(stored, f ,indent=4)

    def reload(self):
        """deserilizes the object from a file"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                obj = json.load(f)
                obj = {key:self.classes(val['__class__'])(**val) for key, val in obj.items()}
                self.__objects = obj
        else:
            return

    def classes(self, class_):
        """returns the class so it can be called somwhere else"""
        from models.base_model import BaseModel
        from models.user import User
        cl = {'BaseModel': BaseModel, 
              'User': User}
        if class_ in cl:
            return cl[class_]
