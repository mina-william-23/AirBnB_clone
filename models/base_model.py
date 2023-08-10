#!/usr/bin/python3
""" BaseModel module that defines BaseModel class """


from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    class BaseModel that defines all common attributes
    methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """ basemodel constructor """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        self.__setattr__(key, datetime.fromisoformat(value))
                    else:
                        self.__setattr__(key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def save(self):
        """ update time of self.updated_at """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ convert attributes to dictionary key-value """
        dc = self.__dict__.copy()
        # dc['id'] = self.id
        dc['__class__'] = self.__class__.__name__
        dc['created_at'] = self.created_at.isoformat()
        dc['updated_at'] = self.updated_at.isoformat()
        return dc

    def __str__(self):
        """
        print the instance class as follows format
        [<class name>] (<self.id>) <self.__dict__>
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
