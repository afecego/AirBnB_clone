#!/usr/bin/python3
"""create class Storage"""
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
    """serializes instances to a JSON file and deserializes JSON file"""
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
        """Construct method to serialize instances"""

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        new_dic = {}
        for key, obj in self.__objects.items():
            new_dic[key] = obj.to_dict()

        with open(self.__file_path, "w") as f:
            f.write(json.dumps(new_dic))

    def reload(self):
        """deserializes the JSON file to __objects"""
        dic_tem = {}
        try:
            with open(self.__file_path, "r") as f:
                dic_tem = json.loads(f.read())
                for key, val in dic_tem.items():
                    self.__objects[key] = self.cla_dic[val["__class__"]](**val)
        except FileNotFoundError:
            pass
