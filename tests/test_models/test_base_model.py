#!/usr/bin/python3
"""Defines unittests for models/base_model.py.
"""
import os
import io
import sys
import models
import unittest
from datetime import datetime
# from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """test instantiation of the BaseModel class."""

    def test_istance_not_none(self):
        self.assertIsNotNone(BaseModel())

    def test_istance_of_basemodel(self):
        self.assertIsInstance(BaseModel(), BaseModel)

    def test_instace_with_kwargs(self):
        kwargs = {
                'my_number': 89, 'name': 'My First Model',
                '__class__': 'BaseModel',
                'updated_at': '2017-09-28T21:05:54.119572',
                'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
                'created_at': '2017-09-28T21:05:54.119427'}
        self.assertIsInstance(BaseModel(**kwargs), BaseModel)

    def test_instance_with_args(self):
        args = (10, "mina")
        self.assertIsNotNone(BaseModel(*args))
        self.assertIsInstance(BaseModel(*args), BaseModel)

    def test_instance_id_uuid(self):
        self.assertIsInstance(BaseModel().id, str)

    def test_instance_datetime_createdate(self):
        self.assertIsInstance(BaseModel().created_at, datetime)

    def test_instance_datetime_updatedate(self):
        self.assertIsInstance(BaseModel().updated_at, datetime)


class Test_BaseModel_Save(unittest.TestCase):
    """ test save function in BaseModel class"""

    def test_save_fun(self):
        bs = BaseModel()
        bs_createdate = bs.created_at
        bs_updatedate = bs.updated_at
        self.assertEqual(bs_createdate, bs_updatedate)
        bs.save()
        bs_updatedate = bs.updated_at
        self.assertNotEqual(bs_createdate, bs_updatedate)


class Test_BaseModel_todict(unittest.TestCase):
    """test to_dict fun in BaseModel class"""

    def test_class_name(self):
        bs = BaseModel()
        bs_dict = bs.to_dict()
        self.assertEqual(bs_dict['__class__'], 'BaseModel')

    def test_createtime_isoformat(self):
        bs = BaseModel()
        bs_dict = bs.to_dict()
        self.assertEqual(bs_dict['created_at'], bs.created_at.isoformat())

    def test_updatetime_isoformat(self):
        bs = BaseModel()
        bs_dict = bs.to_dict()
        self.assertEqual(bs_dict['updated_at'], bs.updated_at.isoformat())


class Test_BaseModel_str(unittest.TestCase):
    """test __str__ fun in BaseModel class"""

    def test_class_str(self):
        bs = BaseModel()
        bs_class_name = bs.__class__.__name__
        bs_dict = {key: value for key, value in bs.__dict__.items() if value}
        str_rep = "[{}] ({}) {}".format(bs_class_name, bs.id, bs_dict)
        self.assertEqual(str_rep, bs.__str__())

    def test_class_print(self):
        bs = BaseModel()
        bs_class_name = bs.__class__.__name__
        bs_dict = {key: value for key, value in bs.__dict__.items() if value}
        str_rep = "[{}] ({}) {}\n".format(bs_class_name, bs.id, bs_dict)

        capturedOutput = io.StringIO()
        # Create StringIO object
        sys.stdout = capturedOutput
        #  and redirect stdout.
        print(bs)
        printed_str = capturedOutput.getvalue()
        self.assertEqual(str_rep, printed_str)
        sys.stdout = sys.__stdout__             # Reset redirect.


if __name__ == "__main__":
    unittest.main()
