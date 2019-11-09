#!/usr/bin/python3
from models.__init__ import storage
"""
Base class
"""

import uuid
import datetime

class BaseModel:
    def __init__ (self, *args, **kwargs):
        if 'id' in kwargs:
            self.id = kwargs['id']
        if 'created_at' in kwargs:
            self.created_at = datetime.datetime.strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
        if 'updated_at' in kwargs:
            self.updated_at = datetime.datetime.strptime(kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)
    def __str__(self):
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__ )
    def save(self):
            self.updated_at = datetime.datetime.now()
            storage.save()
    def to_dict(self):
            dictionary = self.__dict__.copy()
            dictionary['class'] = self.__class__.__name__
            dictionary['created_at'] = self.created_at.isoformat()
            dictionary['updated_at'] = self.updated_at.isoformat()
            return dictionary
