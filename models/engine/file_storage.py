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
    __objects = {}

    def new(self, obj):
        """ adds object to storage
                -Create key as [class name].[id]
                -Add obj to dictionary
                """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def all(self):
        """ returns all objects """
        return self.__objects

    def save(self):
        """ serialize dictionary to json file 
            - Convert obj to dictionary (format)
            - Open file in write
            - Write into file as json"""
        dict = {}

        for key, value in self.__objects.items():
            dict[key] = value.to_dict()

        with open(self.__file_path, 'w') as file_w:
            json.dump(dict, file_w)

    def reload(self):
        """ deserialize json file to __objects
                -If file exists open on read only
                -Load json file to dictionary
                -Import Base class to manage circular import
                -Convert dictionary to objects
            """
        if os.path.exist(self.__file_path):
            with open(self.__file_path, 'r') as file_r:
                dict = json.load(file_r)

        from models.base_model import BaseModel
        for k, v in dict.items():
            self.__objects[k] = BaseModel(**v)
