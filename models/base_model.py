#!/usr/bin/python3
""" BaseModel module that defines BaseModel class """


from uuid import uuid4
from datetime import datetime
import models


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
            models.storage.new(self)

    def save(self):
        """ update time of self.updated_at """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ convert attributes to dictionary key-value """
        dc = {key: value for key, value in self.__dict__.items() if value}
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
        dc = {key: value for key, value in self.__dict__.items() if value}
        return "[{}] ({}) {}".format(class_name, self.id, dc)

    @classmethod
    def count(cls):
        """ count class method to count class in objects in storage class """
        cnt = 0
        name = cls.__name__
        dc = models.storage.all()
        for value in dc.values():
            if value.__class__.__name__ == name:
                cnt += 1
        print(cnt)

    @classmethod
    def all(cls):
        """ all return all created instances of cls in storage instance """
        name = cls.__name__
        dc = models.storage.all()
        li = []
        for value in dc.values():
            if value.__class__.__name__ == name:
                li.append(value.__str__())
        print(li)

    @classmethod
    def show(cls, id):
        """show the object.__str__ by id"""
        name = cls.__name__
        key = ".".join([name, id])
        dc = models.storage.all()
        if key in dc:
            print(dc[key])
        else:
            print("** no instance found **")

    @classmethod
    def destroy(cls, id):
        """ destrory instance with id in stoarge objects list """
        name = cls.__name__
        key = ".".join([name, id])
        dc = models.storage.all()
        if key in dc:
            del dc[key]
            models.storage.save()
        else:
            print("** no instance found **")
