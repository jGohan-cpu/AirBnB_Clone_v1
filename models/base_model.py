#!/usr/bin/python3
'''
defined class BaseModel
'''
import uuid
from datetime import datetime


class BaseModel:
    '''
    contains objects
    BaseModel
    '''

    def __init__(self, *args, **kwargs):
        '''
        construction function for objects
        '''
        if kwargs:
            kwargs.pop('__class__', None)
            self.__dict__.update(kwargs)
            self.created_at = datetime.strptime(
                self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(
                self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        '''
        represents object as string
        '''
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        '''
        saves updated updated object
        '''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''
        converts object into dictionary representation
        '''
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['created_at'] = self.updated_at.isoformat()
        return data
