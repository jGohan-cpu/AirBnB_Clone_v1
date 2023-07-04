#!/usr/bin/python3
""" User class that inherits form BaseModel"""

BaseModel = models.base_model.BaseModel


class User(BaseModel):
    """User class
    Attributes:
        email (str): user email
        password (str): user password
        first_name (str): user first name
        last_name (str): user last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        pass
