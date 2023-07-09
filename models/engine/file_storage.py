#!/usr/bin/python3
"""File_storage, desrializes and serialiazes objects """

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.place import Place


class FileStorage:
    """Function class to serialize (json) file and deserialize file to instance

    __file_path: data storage path
    __objects: dictionary of instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ serialize dictionary to json file 
            - Convert obj to dictionary (format)
            - Open file in write
            - Write into file as json"""
        return self.__objects

    def new(self, obj):
        """Sets in new object to objects"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Objects are serialized and saved in a JSON file"""
        dict = {}

        for key, value in self.__objects.items():
            dict[key] = value.to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(dict, file)

    def reload(self):
        """ deserialize json file to __objects
                -If file exists open on read only and read
                -Load json file to dictionary
                -Eval class name
                -Convert dictionary to objects
                - Otherwise do nothing
            """
        try:
            with open(self.__file_path, "r") as file:
                # Load the JSON data from the file
                json_data = json.load(file)
                # Clear the existing objects
                self.__objects.clear()

                # Iterate over the key-value pairs in the JSON data
                for key, value in json_data.items():
                    # Get the class name from the '__class__' key
                    class_name = value['__class__']
                    # Create an object based on the class name
                    if class_name == 'User':
                        self.__objects[key] = User(**value)
                    elif class_name == 'Place':
                        self.__objects[key] = Place(**value)
                    elif class_name == 'Amenity':
                        self.__objects[key] = Amenity(**value)
                    elif class_name == 'Review':
                        self.__objects[key] = Review(**value)
                    elif class_name == 'State':
                        self.__objects[key] = State(**value)
                    elif class_name == 'City':
                        self.__objects[key] = City(**value)
                    else:
                        self.__objects[key] = BaseModel(**value)
        except Exception:
            # if the file is not found do nothing
            pass
