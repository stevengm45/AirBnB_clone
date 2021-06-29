#!/usr/bin/python3
"""
    Contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    class HBNBCommand that contains entry point of command interpreter
    """
    intro = 'Welcome to hbnb console :)'
    prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel,
               'User': User,
               'State': State,
               'City': City,
               'Amenity': Amenity,
               'Place': Place,
               'Review': Review}

    def emptyline(self):
        """This function shouldn’t execute anything
        """
        pass

    def do_EOF(self, line):
        """End of file to exit the program
        """
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        raise SystemExit

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it and prints the id
        Usage: create <class name>
        """
        args = str.split(line)

        if len(args) < 1:
            print("** class name missing **")
            return False

        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return False
        else:
            new_instance = self.classes[args[0]]()
            print(new_instance.id)
            new_instance.save()
            return False

    def do_show(self, line):
        """Prints the string representation of an instance based on the class and id
        Usage: show <class name> <id>
        """
        args = str.split(line)
        if len(args) < 1:
            print("** class name missing **")
            return False

        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return False

        if len(args) < 2:
            print("** instance id missing **")
            return False

        all_objects = storage.all()
        obj = args[0] + "." + args[1]

        if obj not in all_objects.keys():
            print("** no instance found **")
        else:
            obj_id = all_objects[obj]
            print(obj_id)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        Usage: destroy <class name> <id>
        """
        args = str.split(line)
        if len(args) < 1:
            print("** class name missing **")
            return False

        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return False

        if len(args) < 2:
            print("** instance id missing **")
            return False

        all_objects = storage.all()
        obj = args[0] + "." + args[1]

        if obj not in all_objects:
            print("** no instance found **")
        else:
            all_objects.pop(obj)
            storage.save()
