#!/usr/bin/python3
""" FileStorage module responsbile for serialization and deserialization """


import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    class FileStorage that serializes instances to a JSON
    file and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return dictionary of all objects in __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ append obj to __objects """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serliaze __objects to file path """
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            dc = {}
            for key, value in FileStorage.__objects.items():
                dc[key] = value.to_dict()
            json.dump(dc, f)

    def reload(self):
        """ deserialize from file path into __objects """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                dc = json.load(f)
                obj = FileStorage.__objects
                for key, value in dc.items():
                    obj[key] = eval(value['__class__'])(**value)
        except Exception:
            pass
