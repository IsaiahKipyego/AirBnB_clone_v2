#!/usr/bin/python3
"""defines a class to manage file storage"""
import json


class FileStorage:
    """manages storage models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Return dict of models currently in storage"""
        if cls is not None:
            newobjs = {}
            for key, val in FileStorage.__objects.items():
                if isinstance(val, cls):
                    newobjs[key] = val
            return newobjs

        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dict"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dict to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def delete(self, obj=None):
        """ Deletes obj"""
        if obj is None:
            return
        if obj in FileStorage.__objects.values():
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            del FileStorage.__objects[key]

    def reload(self):
        """Loads storage dic from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except Exception as e:
            pass

    def close(self):
        """
        calls the reload method for deserializing the JSON file
        """
        self.reload()
