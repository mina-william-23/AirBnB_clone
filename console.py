#!/usr/bin/python3
""" console module """

import cmd


class HBNBCommand(cmd.Cmd):
    """ subclass of Cmd class """

    def __init__(self):
        """ HBNB constructor """
        super().__init__()  # Corrected super() call
        self.prompt = '(hbnb) '

    def do_EOF(self, line):
        """ EOF function """
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """Overload emptyline of superclass
        to make it not print the previous command
        if line is empty
        """
        pass


if __name__ == '__main__':  # Corrected __name__ check
    HBNBCommand().cmdloop()
