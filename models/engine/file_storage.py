#!/usr/bin/python3
""" FileStorage module responsbile for serialization and deserialization """


import json
from models.base_model import BaseModel


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
            dc = {key:value.to_dict() for key, value in FileStorage.__objects.items()}
            json.dump(dc, f)

    def reload(self):
        """ deserialize from file path into __objects """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                dc = json.load(f)
                FileStorage.__objects = {key:BaseModel(**value) for key, value in dc.items()}
        except Exception:
            pass
