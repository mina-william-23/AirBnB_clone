#!/usr/bin/python3
""" FileStorage module responsbile for serialization and deserialization """


import json


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
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """ serliaze __objects to file path """
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """ deserialize from file path into __objects """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                FileStorage.__objects = json.load(f)
        except Exception:
            pass
