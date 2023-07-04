#!/usr/bin/python3
""" Review class that inherits from BaseModel"""

BaseModel = models.base_model.BaseModel


class City(BaseModel):
    """stay Review class
    Attributes:
        place_id (str): stay identifier (Place.id)
        user_id (str): user identifier (User.id)
        text (str): review
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args):
        pass
