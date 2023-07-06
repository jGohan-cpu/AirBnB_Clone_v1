#!/usr/bin/python3
""" Review class that inherits from BaseModel"""

BaseModel = models.base_model.BaseModel


class Review(BaseModel):
    """stay Review class
    Attributes:
        place_id (str): stay identifier (Place.id)
        user_id (str): user identifier (User.id)
        text (str): review
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, **kwarg):
        """Kwargs user: user_id, place: place_id, description: user input"""
        self.user_id = kwarg["user_id"]
        self.place_id = kwarg["place_id"]
        self.description = kwarg["description"]

    @property
    def review(self):
        return self.description
