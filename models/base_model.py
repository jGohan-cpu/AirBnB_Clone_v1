#!/usr/bin/python3
"""
This module contains the BaseModel class which will be the base class for
other classes.
"""


import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    A base class named Base Model
    """

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            now = datetime.now()
            self.created_at = now
            self.updated_at = now

    def __str__(self):
        '''
        retuns object as string
        '''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the 'updated_at' attribute with the current date
        and time.
        - Saves instance to storage variable created at __init__
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of the
        instance's __dict__.
        """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
