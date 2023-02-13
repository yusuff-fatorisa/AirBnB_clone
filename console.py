#!/usr/bin/python3
"""Defines the HBnB console"""
import cmd
from models.base_model import BaseModel
from models import storage
import re
from shlex import split


def parse(arg):
    """Takes in command line argument(s) and sieves
    out relevant commands for use"""
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.
        Attributes:
        prompt (str): The command prompt.
        """
    prompt = "(hbnb) "
    __classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
            }

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

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""
        command = parse(line)
        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(command[0])().id)
            storage.save()

    def do_show(self, line):
        """ Prints the string representation of
        an instance based on the class name and id"""
        command = parse(line)
        obj_dict = storage.all()

        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(command) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(command[0], command[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(command[0], command[1])])


    def do_destroy(self, line):
        """ Deletes an instance based on the class
        name and id (save the change into the JSON file)"""

    def do_all(self, line):
        """Prints all string representation of all
        instances based or not on the class name"""

    def do_update(self, line):
        """Updates an instance based on the class
        name and id by adding or updating attribut
        e (save the change into the JSON file)"""


if __name__ == '__main__':
    HBNBCommand().cmdloop()
