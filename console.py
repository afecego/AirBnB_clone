#!/usr/bin/python3
"""Create file consola"""
import cmd
import shlex
import models
from models.base_model import BaseModel
from models.user import User, State, City, Amenity, Place, Review


class HBNBCommand(cmd.Cmd):
    """contains the entry point of the command interpreter"""
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
        """Exit command to exit the program\n"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """Don't do anything"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")

        elif arg not in self.dicc:
            print("** class doesn't exist **")

        else:
            base_model = BaseModel()
            print(base_model.id)
            base_model.save()

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        token = arg.split(" ")
        if not token[0]:
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
        """Deletes an instance based on the class name and id"""
        token = arg.split(" ")
        if not token[0]:
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
        """Prints all string representation of all instances"""
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
        """Updates an instance based on the class name and id"""
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
