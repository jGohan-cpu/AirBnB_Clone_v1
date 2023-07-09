#!/usr/bin/python3

"""This module contains the BaseModel class which will be the base class for
other classes."""
import uuid
from datetime import datetime


class BaseModel:
    """a baseclass named basemodel"""

    def __init__(self, *args, **kwargs):
        """constructor method"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def updated(self):
        """update method"""
        self.updated_at = datetime.now()

    def __str__(self):
        """retuns object as string"""
        class_name = type(self).__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """ updates the 'updated_at' attribute with the current date
        and time.
        - Saves instance to storage variable created at __init__"""
        self.updated_at = datetime.now()
        from models import storage
        storage.new(self)
        storage.save()

    def to_dict(self):
        """convert and returns dictionary method"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict