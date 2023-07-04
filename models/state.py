#!/usr/bin/python3
""" State class that inherits from BaseModel"""

BaseModel = models.base_model.BaseModel


class State(BaseModel):
    """State class
    Attributes:
        name (str): name of state
    """

    name = ""

    def __init__(self, name=None):
        self.name = name

    @property
    def state(self):
        return self.name
