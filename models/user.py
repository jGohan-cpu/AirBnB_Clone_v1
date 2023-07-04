#!/usr/bin/python3
""" User class that inherits form BaseModel"""

BaseModel = models.base_model.BaseModel


class User(BaseModel):
    """User class
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, email, password, first_name, last_name):
        """Creates a new User

        Attributes:
        email (str): user email
        password (str): user password
        first_name (str): user first name
        last_name (str): user last name

        """
        self.email = email
        self.__password = password
        self.first_name = first_name
        self.last_name = last_name

    """crud functions: create, read, update delete"""

    @property
    def user_email(self):
        return self.email

    @property
    def user_name(self):
        return (self.first_name + " " + self.last_name)
