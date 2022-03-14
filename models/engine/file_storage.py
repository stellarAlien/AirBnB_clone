#!/usr/bin/python3
"""
module of file storage
handles json objects
"""

import json
from models.base_model import BaseModel


class FileStorage:
    """
    class responsible for 
    storing instances
    """
    __file_path = "file.json"
    __objects = {}
    classes = {'BaseModel'}
    
    def all(self):
        """
        returns objects
        """
        return self.__objects

    def new(self, obj):
        """
        updates obj dict
        """
        self.__objects[str(obj.__class__.__name__+ '.' + obj.id)] = obj

    def save(self):
        """
        saves objects dict to file
        in json format
        """
        for key, val in FileStorage.__objects.items():
            self.__objects[key] = val.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f)

    def reload(self):
        """
        makes json file to py object 
        """
        try:
            with open(self.__file_path, 'r') as f:
                new_dict = json.load(f)
            for key, val in new_dict.items():
                classes = k.split('.')[0]
                self.__objects[k] = eval(classes)(**v)
        except:
            pass
