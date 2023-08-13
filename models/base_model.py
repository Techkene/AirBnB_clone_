#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
from engine import file_storage
""" Class that other objects inherit from """
tfomat = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """ Instantiate a new model"""
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            kwargs['updated_at'] = datetime.strptime(['updated_at'], tfomat)
            kwargs['created_at'] = datetime.strptime(['created_at'], tfomat)
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        return("[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.dict__)
               )

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.update_at = datatime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
