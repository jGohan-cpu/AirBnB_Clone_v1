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
