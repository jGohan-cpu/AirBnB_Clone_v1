#!/usr/bin/python3
""" Contains the entry point of the command interpreter """
import cmd


class HBNBCommand(cmd.Cmd):
    """ Command Class """
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Function to exit the program"""
        return True

    def do_EOF(self, args):
        """Function to exit the program"""
        return True

    def emptyline(self):
        """If empty do nothing"""
        pass

    def help_quit(self):
        """Help message for quit command"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Help message for EOF command"""
        print("Function to exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
