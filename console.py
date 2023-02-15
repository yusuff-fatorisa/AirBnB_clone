#!/usr/bin/python3
"""Defines the HBnB console"""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


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
        command = parse(line)
        obj_dict = storage.all()

        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(command) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(command[0], command[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(command[0], command[1])]
            storage.save()

    def do_all(self, line):
        """Prints all string representation of all
        instances based or not on the class name"""
        command = parse(line)

        if len(command) > 0 and command[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(command) > 0 and command[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(command) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_count(self, line):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        command = parse(line)
        count = 0
        for obj in storage.all().values():
            if command[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, line):
        """Updates an instance based on the class
        name and id by adding or updating attribut
        e (save the change into the JSON file)"""
        command = parse(line)
        objdict = storage.all()

        if len(command) == 0:
            print("** class name missing **")
            return False
        if command[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(command) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(command[0], command[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(command) == 2:
            print("** attribute name missing **")
            return False
        if len(command) == 3:
            try:
                type(eval(command[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(command) == 4:
            obj = objdict["{}.{}".format(command[0], command[1])]
            if command[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[command[2]])
                obj.__dict__[command[2]] = valtype(command[3])
            else:
                obj.__dict__[command[2]] = command[3]
        elif type(eval(command[2])) == dict:
            obj = objdict["{}.{}".format(command[0], command[1])]
            for k, v in eval(command[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
