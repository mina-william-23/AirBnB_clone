#!/usr/bin/python3
""" console module """

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models
from helper import valid_classes


class HBNBCommand(cmd.Cmd):
    """ subclass of Cmd class """
    def __init__(self):
        """ HBNB constructor """
        super().__init__()
        self.prompt = '(hbnb) '

    def do_EOF(self, line):
        """ EOF function """
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """
        Overload emptyline of superclass
        to make it not print the previous command
        if line is empty
        """
        pass

    def do_create(self, obj_name):
        """Creates a new instance of BaseModel"""
        if not obj_name:
            print("** class name missing **")
        elif obj_name not in valid_classes:
            print("** class doesn't exist **")
        else:
            # instance = globals()[obj_name]()
            instance = eval(obj_name)()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """
        Prints the string representation of
        an instance based on the class name and id
        """
        if not line:
            print("** class name missing **")
            return

        args = line.split(' ')
        if args[0] not in valid_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] in valid_classes:
            key = ".".join([args[0], args[1]])
            dc = models.storage.all()
            if key in dc:
                print(dc[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        if args[0] not in valid_classes:
                print("** class doesn't exist **")
        elif len(args) == 1:
                print("** instance id missing **")
        elif args[0] in valid_classes:
            key = ".".join(args)
            dc = models.storage.all()
            if key in dc:
                del dc[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of
        all instances based or not on the class name
        """
        if not line:
            dc = models.storage.all()
            li = [value.__str__() for value in dc.values()]
            print(li)
        else:
            if line in valid_classes:
                dc = models.storage.all()
                li = []
                for value in dc.values():
                    if value.__class__.__name__ == line:
                        li.append(value.__str__())
                print(li)
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        args = line.split()
        length = len(args)
        if not args:
            print("** class name missing **")
        elif args[0] not in valid_classes:
                print("** class doesn't exist **")
        elif len(args) == 1:
                print("** instance id missing **")
        elif length >= 2:
            key = ".".join(args[:2])
            dc = models.storage.all()
            if key in dc:
                try:
                    if args[2]:
                        try:
                            if args[3]:
                                if type(eval(args[3])) in [str, int, float]:
                                    dc[key].__setattr__(args[2], eval(args[3]))
                                    dc[key].save()
                        except IndexError:
                            print("** value missing **")
                except IndexError:
                    print("** attribute name missing **")
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
