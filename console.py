#!/usr/bin/python3
""" Contains the entry point of the command interpreter """
import cmd
from models import storage
from models import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Command Class """
    prompt = "(hbnb)"

    def __init__(self):
        super(HBNBCommand, self).__init__()

    def quit(self, args):
        """Function to exit program"""
        pass

    def EOF(self, args):
        """Function to exit program"""
        return self.quit(args)

    def empty(self):
        """If empty do nothing"""
        pass

    if __name__ == "__main__":
        HBNBCommand()
