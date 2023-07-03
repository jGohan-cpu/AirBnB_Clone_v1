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

    def __init__(self):
        '''
        construction function for objects
        '''
        self.id = str(uuid.uuid4)
        self.created_at = datetime.now()
        self.updated_at = self.created.at

    def __str__(self):
        '''
        represents object as string
        '''
        class_name = self.__class__.__name__
        return (f"[{class_name}] ({self.id}) {self.__dict__}")

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
