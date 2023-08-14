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

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "f.json")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("f.json", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        fs = FileStorage()
        self.assertIsInstance(fs.all(), dict)
        for v in fs.all().values():
            self.assertIsInstance(v, BaseModel)

    def test_new(self):
        fs = FileStorage()
        bs = BaseModel()
        self.assertIn(bs, fs.all().values())

    def test_save_method(self):
        bs = BaseModel()
        key = ".".join([bs.__class__.__name__, bs.id])
        models.storage.save()
        with open("file.json", "r") as f:
            rd = json.load(f)
            self.assertIn(key, rd)

    def test_save_method_update(self):
        b_m_c = BaseModel()
        u_s_c = User()
        s_t_c = State()
        p_l_c = Place()
        c_y_c = City()
        a_m_c = Amenity()
        r_v_c = Review()
        models.storage.new(b_m_c)
        models.storage.new(u_s_c)
        models.storage.new(s_t_c)
        models.storage.new(p_l_c)
        models.storage.new(c_y_c)
        models.storage.new(a_m_c)
        models.storage.new(r_v_c)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + b_m_c.id, save_text)
            self.assertIn("User." + u_s_c.id, save_text)
            self.assertIn("State." + s_t_c.id, save_text)
            self.assertIn("Place." + p_l_c.id, save_text)
            self.assertIn("City." + c_y_c.id, save_text)
            self.assertIn("Amenity." + a_m_c.id, save_text)
            self.assertIn("Review." + r_v_c.id, save_text)

    def test_save_method_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload_method(self):
        b_m_c = BaseModel()
        u_s_c = User()
        s_t_c = State()
        p_l_c = Place()
        c_y_c = City()
        a_m_c = Amenity()
        r_v_c = Review()
        models.storage.new(b_m_c)
        models.storage.new(u_s_c)
        models.storage.new(s_t_c)
        models.storage.new(p_l_c)
        models.storage.new(c_y_c)
        models.storage.new(a_m_c)
        models.storage.new(r_v_c)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + b_m_c.id, objs)
        self.assertIn("User." + u_s_c.id, objs)
        self.assertIn("State." + s_t_c.id, objs)
        self.assertIn("Place." + p_l_c.id, objs)
        self.assertIn("City." + c_y_c.id, objs)
        self.assertIn("Amenity." + a_m_c.id, objs)
        self.assertIn("Review." + r_v_c.id, objs)

    def test_reload_method_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
