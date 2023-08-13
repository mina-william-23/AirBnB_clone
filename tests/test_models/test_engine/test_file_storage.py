#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.
"""
import os
import io
import sys
import models
import unittest
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class Test_FileStorage_instantiation(unittest.TestCase):
    """test instantiation of the FileStorage class."""

    def test_not_none(self):
        fs = FileStorage()
        self.assertIsNotNone(fs)

    def test_instance(self):
        fs = FileStorage()
        self.assertIsInstance(fs, FileStorage)
        
    def test_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

class Test_FileStorage_all(unittest.TestCase):
    """ test fun all in filestorage class """

    def test_all(self):
        fs = FileStorage()
        self.assertIsInstance(fs.all(), dict)
        for v in fs.all().values():
            self.assertIsInstance(v, BaseModel)

    def test_new(self):
        fs = FileStorage()
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)
        self.assertIn(bm, fs.all().values())
        self.assertIn(us, fs.all().values())
        self.assertIn(st, fs.all().values())
        self.assertIn(pl, fs.all().values())
        self.assertIn(cy, fs.all().values())
        self.assertIn(am, fs.all().values())
        self.assertIn(rv, fs.all().values())

    def test_save(self):
        bs = BaseModel()
        key = ".".join([bs.__class__.__name__, bs.id])
        models.storage.save()
        with open("file.json", "r") as f:
            rd = json.load(f)
            self.assertIn(key, rd)

    def test_reload(self):
        bs = BaseModel()
        models.storage.save()
        models.storage.reload()
        md_all = models.storage.all()
        key = ".".join([bs.__class__.__name__, bs.id])
        self.assertIn(key, md_all)


if __name__ == "__main__":
    unittest.main()
