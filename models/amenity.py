#!/usr/bin/python3
"""
Module containing the Amenity
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class - dictionary of amenities
    Attributes:
        name (str): name of amenity
    """
    name = ""
