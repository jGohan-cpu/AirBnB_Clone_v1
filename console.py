#!/usr/bin/python3
"""
    The console for the AirBnB project.
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models import storage
from models.state import State
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Console console class 
    to execute commands"""
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing when an empty line is entered
        in the command prompt"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel. It also saves the id
        of the new object and prints the id"""

        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg)()

            new_instance.save()

            print(new_instance.id)

        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Print the string representation of an object"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ["BaseModel", "User", "Place", "Amenity", "Review", "State", "City"]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        instances = storage.all()

        if key in instances:
            instance = instances[key]
            print(instance)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ["BaseModel", "User", "Place", "Amenity", "Review", "State", "City"]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        instances = storage.all()

        if key in instances:
            del instances[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Print all string representations of instances."""
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
        else:
            args = arg.split()
            class_name = args[0]
            if class_name not in ["BaseModel", "User", "Place", "Amenity", "Review", "State", "City"]:
                print("** class doesn't exist **")
                return
        print([str(obj) for obj in objects.values() if isinstance(obj, globals()[class_name])])

    def do_update(self, arg):
        """Update an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            instance_id = args[1]
            key = class_name + '.' + instance_id
            instance = storage.all().get(key)
            if not instance:
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            attr_name = args[2]
            attr_value = args[3]
            if hasattr(instance, attr_name):
                attr_type = type(getattr(instance, attr_name))
                setattr(instance, attr_name, attr_type(attr_value))
                instance.save()
            else:
                print("** attribute doesn't exist **")
        except IndexError:
            if len(args) < 2:
                if args[0] not in ["BaseModel"]:
                    print("** class doesn't exist **")
                else:
                    print("** instance id missing **")
            else:
                print("** no instance found **")

    def do_EOF(self, arg):
        """End of file command to exit the command prompt"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the command prompt"""
        return True


if __name__ == '__main__':

    HBNBCommand().cmdloop()
