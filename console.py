#!/usr/bin/python3
import cmd
import datetime
import uuid


class BaseModel:
    def __init__(self):
        self.id = uuid.uuid4()
        self.create_at = datetime.datetime.now()
        self.update_at = datetime.datetime.now()


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the console"""
        return True

    def do_print(self, line):
        """Print Hilary and Yusuff"""
        print("Hilary and Yusuff")

    def do_create(self, line):
        """Create an user"""
        user = BaseModel()
        print(user.id, user.create_at, user.update_at)

    def do_help(self, line):
        """
        Print the list of available commands
        and their brief descriptions
        """
        print("Commands:")
        for cmd in self.get_names():
            if cmd.startswith("do_"):
                gta = self.__getattribute__(cmd).__doc__
                print("  %s: %s" % (cmd[3:]), gta)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
