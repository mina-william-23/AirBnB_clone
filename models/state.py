#!/usr/bin/python3
"""state module """


from models.base_model import BaseModel


class State(BaseModel):
    """ State Class subclass of BaseModel """

    name = ""

    def __init__(self, *args, **kwargs):
        """State class constructor"""
        super().__init__(*args, **kwargs)
