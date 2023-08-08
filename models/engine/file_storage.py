#!/usr/bin/python3
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
                self.__objects[f"{type(obj).__name__}.{obj.id}"] = obj
                
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
                                obj = {key:self.classes()(**val) for key, val in obj.items()}
                                # for key,val in obj.items():
                                #         cl = val["__class__"]
                                #         FileStorage.__objects[key] = cl(**val)
                                FileStorage.__objects = obj
                                # print(obj)
                                # print(FileStorage.__objects)
                                # self.__objects = obj
                                # print(self.__objects)
                else:return
                
        def classes(self):
                """returns the class so it can be called somwhere else"""
                from models.base_model import BaseModel
                cl = BaseModel
                return cl