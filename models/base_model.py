#!/usr/bin/python3
"""
base model thatall subbsequent classes
inherit from
"""

from datetime import datetime
import json
import models
import time
import uuid
#from models.engine.file_storage import FileStorage

class BaseModel():
    """
    primordial attributes
    """
    def __init__(self, *args, **kwargs):
        """
        #initialize with basic attributes
        """
        if(kwargs):
            if "created_at" in kwargs:
                self.created_at = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            if("updated_at" in kwargs):
                self.updated_at = datetime.strptime(datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S.%f"), "%Y-%m-%dT%H:%M:%S.%f")
            if("__class__" in kwargs):
                pass
            if("name" in kwargs):
                self.name = kwargs["name"]
            if("id" in kwargs):
                self.id = kwargs["id"]
            if("my_number" in kwargs):
                self.my_number = kwargs["my_number"]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = self.created_at
            self.first_name = ""
            self.email= ""
            models.storage.new(self)

    def __str__(self):
        """string represantaion of instance"""
        return("[{:s}] ({:}) {:}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        saves update time
        """
        self.__dict__.update(updated_at = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S.%f"))
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values 
        of __dict__ of the instance
        """
        d = self.__dict__.copy()
        d.update(__class__ = self.__class__.__name__)
        return d 
