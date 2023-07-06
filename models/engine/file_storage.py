#!/usr/bin/python3
"""
File Storage of class
"""
import json
BaseModel = model.base_model.BaseModel
"""
User = model.user.User
State = models.state.State
City = models.city.City
Place = models.place.Place
Amenity = models.amenity.Amenity
Review = models.review.Review
"""


class FileStorage():
    """Function class to serialize (json) file and deserialize file to instance

    __file_path: data storage path
    __objects: dictionary of instances
    """
    __file_path = "file.json"
    __instances = {}

    def new(self, obj):
        """ adds object to objects """
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def all(self):
        """ returns all objects """
        return self.__objects

    def save(self):
        """ serialize dictionary to json file """
        dict = {}
        for key, value in self.__objects.items():
            dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(dict, file)

    except FileNotFoundError:
    pass