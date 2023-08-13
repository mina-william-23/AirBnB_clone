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
from models.user import User
from models.base_model import BaseModel


class TestUser_instantiation(unittest.TestCase):
    """test instantiation of the User class."""

    def test_istance_not_none(self):
        self.assertIsNotNone(User())

    def test_istance_of_basemodel(self):
        self.assertIsInstance(User(), User)

    def test_instace_with_kwargs(self):
        create_time = update_time = datetime.now().isoformat()
        kwargs = {
                'my_number': 89, 'name': 'My second Model',
                '__class__': 'User',
                'updated_at': update_time,
                'id': 'b6a6e20c-c67d-4312-9a75-9d084935e579',
                'created_at': create_time}
        us = User(**kwargs)
        self.assertIsInstance(us, User)
        self.assertEqual(us.my_number, 89)
        self.assertNotIn('__class__', us.__dict__)
        self.assertEqual(create_time, us.created_at.isoformat())
        self.assertEqual(update_time, us.updated_at.isoformat())

    def test_instance_with_args(self):
        args = (10, "mina")
        us = User(*args)
        self.assertIsNotNone(us)
        self.assertIsInstance(us, User)
        self.assertNotIn(10, us.__dict__.values())
        self.assertNotIn("mina", us.__dict__.values())

    def test_instance_id_uuid(self):
        self.assertIsInstance(User().id, str)

    def test_instance_datetime_createdate(self):
        self.assertIsInstance(User().created_at, datetime)

    def test_instance_datetime_updatedate(self):
        self.assertIsInstance(User().updated_at, datetime)

    def test_instance_email(self):
        us = User()
        self.assertIsInstance(us.email, str)
        self.assertEqual(us.email, "")
        us.email = "hello@gmail.com"
        self.assertEqual(us.email, "hello@gmail.com")

    def test_instance_password(self):
        us = User()
        self.assertIsInstance(us.password, str)
        self.assertEqual(us.password, "")
        us.password = 12345678
        self.assertEqual(us.password, 12345678)

    def test_instance_first_name(self):
        us = User()
        self.assertIsInstance(us.first_name, str)
        self.assertEqual(us.first_name, "")
        self.first_name = "mina"
        self.assertEqual(self.first_name, "mina")

    def test_instance_last_name(self):
        us = User()
        self.assertIsInstance(us.last_name, str)
        self.assertEqual(us.last_name, "")
        self.last_name = "alx"
        self.assertEqual(self.last_name, "alx")


if __name__ == "__main__":
    unittest.main()
