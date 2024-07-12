#!/usr/bin/python3

import uuid
from datetime import datetime
import models

class BaseModel:
    """Basemodel for for creating and managing instances"""

    def __init__(self, *args, **kwargs):
        """initialize an instance of the basemodel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        obj_dict =  self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        return obj_dict

    def save(self):
       models.storage.save()

    def __str__(self):
        class_name = self.__class__.__name__

        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)


user = BaseModel()





