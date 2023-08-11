#!/usr/bin/python3
""" This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """ Returns a dictonary of models currently in storage"""
    __file_path = 'file.json'
    __object = {}

    def all(self):
        """Return a dictionary of models currently in storage"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictonary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """ Saves storage dictonary to file """
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'place': Place,
                    'State': State, 'City':City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.item():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
