#!/usr/bin/python3
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
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

    def do_print(self, line):
        """Print Hilary and Yusuff"""
        print("Hilary and Yusuff")

    def do_create(self, line):
        """Create an user"""
        user = BaseModel()
        print(user.id, user.created_at, user.updated_at)

    def do_show(self, line):
        """ Prints the string representation of
        an instance based on the class name and id"""

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
