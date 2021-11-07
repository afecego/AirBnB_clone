#!/usr/bin/python3
"""
Create class Storage
"""
import json
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file

    Attributes
    ----------
    __file_path: str
        path to the JSON file
    __objects: {}
        Contains diccionary empty but will store all objects by <class name>.id
    cla_dic: {}
        Contains the class name directions to his class

    Methods
    -------
    __init__
        (Construct method to serialize instances class FileStorage)
    all
        (Returns the dictionary __objects)
    new
        (Sets in __objects the obj with key <obj class name>.id)
    save
        (Serializes __objects to the JSON file (path: __file_path))
    reload
        (Deserializes the JSON file to __objects)
    """
    __file_path = "file.json"
    __objects = {}
    cla_dic = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def __init__(self):
        """
        Construct method to serialize instances class FileStorage
        """

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        new_dic = {}
        for key, obj in self.__objects.items():
            new_dic[key] = obj.to_dict()

        with open(self.__file_path, "w") as f:
            f.write(json.dumps(new_dic))

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        dic_tem = {}
        try:
            with open(self.__file_path, "r") as f:
                dic_tem = json.loads(f.read())
                for key, val in dic_tem.items():
                    self.__objects[key] = self.cla_dic[val["__class__"]](**val)
        except FileNotFoundError:
            pass
