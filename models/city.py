#!/usr/bin/python3
"""city module """


from models.base_model import BaseModel


class City(BaseModel):
    """ City Class subclass of BaseModel """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """City class constructor"""
        super().__init__(*args, **kwargs)
