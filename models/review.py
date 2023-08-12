#!/usr/bin/python3
"""review module """


from models.base_model import BaseModel


class Review(BaseModel):
    """ review Class subclass of BaseModel """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """review class constructor"""
        super().__init__(*args, **kwargs)
