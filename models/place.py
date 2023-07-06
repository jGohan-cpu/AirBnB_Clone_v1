#!/usr/bin/python3
""" Place class that inherits from BaseModel"""

BaseModel = models.base_model.BaseModel


class Place(BaseModel):
    """Place class
    """

    city_id = 0
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0
    longitude = 0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """ Attributes:
        city_id (str): city identifier

        user_id (str): user identifier

        name (str): name of place

        description (str): description of place

        number_rooms (int): number of rooms

        number_bathrooms (int): number of bathrooms

        max_guest (int): maximum guest

        price_by_night (int): price of stay

        latitude (float): latitude

        longitude (float): longitude

        amenity_ids (str): list of amenities ids"""
        pass
