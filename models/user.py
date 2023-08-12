#!/usr/bin/python3
"""user module """


from models.base_model import BaseModel


class User(BaseModel):
    """ User Class subclass of BaseModel """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """User class constructor"""
        super().__init__(*args, **kwargs)
