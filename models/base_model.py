#!/usr/bin/python3
"""
Create class BaseModel
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Defines all common attributes/methods for other classes

    Methods
    -------
    __init__
        (Constructor of the class BaseModel)
    __str__
        (should print: [<class name>] (<self.id>) <self.__dict__>)
    save
        (updates the public instance attribute updated_at)
    to_dict
        (returns a dictionary containing all keys/values)
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor of the class BaseModel

        Parameters
        ----------
        id: string
            assign with an uuid when an instance is created
        created_at: datetime
            assign with the current datetime when an instance is created
        updated_at: datetime
            assign with the current datetime when an instance is created and it
            will be updated every time you change your object
        """
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

        else:
            fto = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    value = datetime.strptime(value, fto)
                if key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """
        should print: [<class name>] (<self.id>) <self.__dict__>
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                      self.__dict__))

    def save(self):
        """
        updates the public instance attribute updated_at
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        """
        dic = {}
        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()

        return dic
