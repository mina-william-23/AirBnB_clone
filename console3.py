#!/usr/bin/python3
""" Entry point of the command interpreter """
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
import json
import shlex


class HBNBCommand(cmd.Cmd):
    """Command processor"""

    prompt = "(hbnb) "
    l_classes = ['BaseModel', 'User', 'Amenity',
                 'Place', 'City', 'State', 'Review']

    l_c = ['create', 'show', 'update', 'all', 'destroy', 'count']

    def precmd(self, arg):
        """parses command input"""
        if '.' in arg and '(' in arg and ')' in arg:
            cls = arg.split('.')
            cnd = cls[1].split('(')
            args = cnd[1].split(')')
            if cls[0] in HBNBCommand.l_classes and cnd[0] in HBNBCommand.l_c:
                arg = cnd[0] + ' ' + cls[0] + ' ' + args[0]
        return arg

    def help_help(self):
        """ Prints help command description """
        print("Provides description of a given command")

    def emptyline(self):
        """do nothing when empty line"""
        pass

    def do_count(self, cls_name):
        """counts number of instances of a class"""
        count = 0
        all_objs = storage.all()
        for k, v in all_objs.items():
            clss = k.split('.')
            if clss[0] == cls_name:
                count = count + 1
        print(count)

    def do_create(self, obj_name):
        """Creates a new instance of BaseModel"""
        if not obj_name:
            print("** class name missing **")
        elif obj_name not in HBNBCommand.l_classes:
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
        if args[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] in HBNBCommand.l_classes:
            key = ".".join([args[0], args[1]])
            dc = storage.all()
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

        if args[0] not in HBNBCommand.l_classes:
                print("** class doesn't exist **")
        elif len(args) == 1:
                print("** instance id missing **")
        elif args[0] in HBNBCommand.l_classes:
            key = ".".join(args)
            dc = storage.all()
            if key in dc:
                del dc[key]
                storage.save()
            else:
                print("** no instance found **")

    # def do_all(self, arg):
    #     """ Prints string represention of all instances of a given class """

    #     if not arg:
    #         print("** class name missing **")
    #         return

    #     args = arg.split(' ')

    #     if args[0] not in HBNBCommand.l_classes:
    #         print("** class doesn't exist **")
    #     else:
    #         all_objs = storage.all()
    #         list_instances = []
    #         for key, value in all_objs.items():
    #             ob_name = value.__class__.__name__
    #             if ob_name == args[0]:
    #                 list_instances += [value.__str__()]
    #         print(list_instances)
    def do_all(self, line):
        """
        Prints all string representation of
        all instances based or not on the class name
        """
        if not line:
            dc = storage.all()
            li = [value.__str__() for value in dc.values()]
            print(li)
        else:
            if line in HBNBCommand.l_classes:
                dc = storage.all()
                li = []
                for value in dc.values():
                    if value.__class__.__name__ == line:
                        li.append(value.__str__())
                print(li)
            else:
                print("** class doesn't exist **")

    # def do_update(self, arg):
    #     """ Updates an instance based on the class name and id """

    #     if not arg:
    #         print("** class name missing **")
    #         return

    #     # a = ""
    #     # for argv in arg.split(','):
    #     #     a = a + argv

    #     # args = shlex.split(a)
    #     args = arg.split()
    #     if args[0] not in HBNBCommand.l_classes:
    #         print("** class doesn't exist **")
    #     elif len(args) == 1:
    #         print("** instance id missing **")
    #     else:
    #         all_objs = storage.all()
    #         for key, objc in all_objs.items():
    #             ob_name = objc.__class__.__name__
    #             ob_id = objc.id
    #             if ob_name == args[0] and ob_id == args[1].strip('"'):
    #                 if len(args) == 2:
    #                     print("** attribute name missing **")
    #                 elif len(args) == 3:
    #                     print("** value missing **")
    #                 else:
    #                     setattr(objc, args[2], args[3])
    #                     storage.save()
    #                 return
    #         print("** no instance found **")
    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        args = line.split()
        length = len(args)
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.l_classes:
                print("** class doesn't exist **")
        elif len(args) == 1:
                print("** instance id missing **")
        elif length >= 2:
            key = ".".join(args[:2])
            dc = storage.all()
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


    def do_quit(self, line):
        """ Quit command to exit the command interpreter """
        return True

    def do_EOF(self, line):
        """ EOF command to exit the command interpreter """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()