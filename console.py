#!/usr/bin/python3
"""
Create class HBNBCommand
"""
import cmd
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Contains the entry point of the command interpreter

    Attributes
    ----------
    prompt: str
        a formatted string to print out what the animal says
    dicc: []
        Contains the class name directions to his class

    Methods
    -------
    do_EOF
        (Exit command to exit the program)
    do_quit
        (Quit command to exit the program)
    emptyline
        (Don't do anything)
    do_create
        (Creates a new instance of BaseModel)
    do_show
        (Prints the string representation of an instance)
    do_destroy
        (Deletes an instance based on the class name and id)
    do_all
        (Prints all string representation of all instances)
    do_update
        (Updates an instance based on the class name and id)
    """
    prompt = "(hbnb) "
    dicc = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_EOF(self, arg):
        """
        Exit command to exit the program\n
        """
        return True

    def do_quit(self, arg):
        """
        Quit command to exit the program\n
        """
        return True

    def emptyline(self):
        """
        Don't do anything\n
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel\n
        """
        if not arg:
            print("** class name missing **")

        elif arg not in self.dicc:
            print("** class doesn't exist **")

        else:
            ins_dic = self.dicc[arg]()
            print(ins_dic.id)
            models.storage.save()

    def do_show(self, arg):
        """
        Prints the string representation of an instance\n
        """
        token = shlex.split(arg)
        if len(token) == 0:
            print("** class name missing **")

        elif token[0] not in self.dicc:
            print("** class doesn't exist **")

        elif len(token) == 1:
            print("** instance id missing **")

        else:
            ins = models.storage.all()
            key = token[0] + "." + token[1]
            if key in ins:
                print(ins[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id\n
        """
        token = shlex.split(arg)
        if len(token) == 0:
            print("** class name missing **")

        elif token[0] not in self.dicc:
            print("** class doesn't exist **")

        elif len(token) == 1:
            print("** instance id missing **")

        else:
            ins = models.storage.all()
            key = token[0] + "." + token[1]
            if key in ins:
                del ins[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances\n
        """
        if len(arg) == 0:
            ins = models.storage.all()
            all = []
            for key in ins:
                x = str(ins[key])
                all.append(x)
            print(all)

        elif arg not in self.dicc:
            print("** class doesn't exist **")

        else:
            ins = models.storage.all()
            all = []
            for key in ins:
                if arg in key:
                    x = str(ins[key])
                    all.append(x)
            print(all)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id\n
        """
        token = shlex.split(arg)
        if len(token) == 0:
            print("** class name missing **")

        elif token[0] not in self.dicc:
            print("** class doesn't exist **")

        elif len(token) == 1:
            print("** instance id missing **")

        else:
            ins = models.storage.all()
            key = token[0] + "." + token[1]
            if key not in ins:
                print("** no instance found **")

            elif len(token) == 2:
                print("** attribute name missing **")

            elif len(token) == 3:
                print("** value missing **")

            elif len(token) > 3:
                actual = ins.get(key)
                setattr(actual, token[2], token[3])
                models.storage.save()

    def default(self, arg):
        """counts the number objects in File Storage"""
        arg = arg.split()
        ins = models.storage.all()
        count = 0
        for key, value in ins.items():
            x = value.__class__.__name__
            key = f"{x}.count()"
            if arg[-1] == key:
                count += 1
        print(count)


if __name__ == '__main__':
    """
    Main of the console
    """
    HBNBCommand().cmdloop()
