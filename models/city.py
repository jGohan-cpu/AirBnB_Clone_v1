#!/usr/bin/python3
"""
City class that inherits from BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class
    Attributes:
        state_id (str): state identifier
        name (str): name of the city
    """
    state_id = ""
    name = ""
