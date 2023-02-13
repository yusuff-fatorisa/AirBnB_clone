#!/usr/bin/python3
"""Defines the HBnB console"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.
        Attributes:
        prompt (str): The command prompt.
        """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the console"""
        return True

    def do_EOF(self, line):
        """End the program at EOF signal"""
        print("")
        return True

    def emptyline(self):
        """Do nothing at empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
