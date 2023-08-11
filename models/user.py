#!/usr/bin/python3
"""user module """


from models.base_model import BaseModel


class User(BaseModel):
    """ User Class subclass of BaseModel """

    def __init__(self, *args, **kwargs):
        """User class constructor"""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
