#!/usr/bin/python3
""" Amenity class that inherits from BaseModel"""

BaseModel = models.base_model.BaseModel


class Amenity(BaseModel):
    """Amenity class - dictionary of amenities
    Attributes:
        name (str): name of amenity
    """
    name = ""

    def __init__(self, **kwargs):
        pass
