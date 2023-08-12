#!/usr/bin/python3
"""amenity.py module """


from models.base_model import BaseModel


class Amenity(BaseModel):
    """ amenity Class subclass of BaseModel """
    name = ""

    def __init__(self, *args, **kwargs):
        """amenity class constructor"""
        super().__init__(*args, **kwargs)
