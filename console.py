#!/usr/bin/python3
"""
module
console.py that contains the entry
point of the command interpreter
"""
import cmd
import sys
import signal
import models
from models import storage
from models.base_model import BaseModel

classes = {"BaseModel"}

class HBNBCommand(cmd.Cmd):
    """
    interactive cmd prompt behavior
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        print()
        return

    def do_create(self, arg):
        """create new instance of BaseModel"""
        if(arg is None):
            print("** class name missing **")
        elif(str(arg) != "BaseModel"):
            print("** class doesn't exist **")
        else:
            x = BaseModel()
            x.save()
            print(x.id)

    def do_show(self, args):
        """ Prints the string representation of an instance
        based on the class name and id
        """
        x = args.split()
        try:
            if(len(x) == 0):
                print("** class name missing **")
                return
            elif(not(str(x[0]) in "BaseModel")):
                print(" ** class doesn't exist **")
                return
            elif(len(x) == 1):
                print("** instance id missing **")
                return
            name = str(x[0] + x[1])
            if(name not in storage.all().keys()):
                print("** no instance found **")
                return
            else:
                print(storage.all()[name])
                return
        except(IndexError):
            print("** instance id missing **")

    def do_destroy(self, args):
        """
        destroys instance based on class and id
        """
        x = list(map(str, args.split()))
        try:
            if(x[0] == ""):
                print("** class name missing **")
            elif(not(str(x[0]) in classes)):
                print("** class doesn't exist **")
            elif(x[1] is None):
                print("** instance id missing **")
            else:
                name = str(x[0] + x[1])
            if(name not in storage.all().keys()):
                print("** no instance found **")
            else:
                del storage.all()[name]
                storage.save()
        except IndexError:
            print("**class name missing**")

    def do_all(self, args):
        """
        displlays instances  based on class otherwise all classes
        """
        x = args.split()
        if(not args  or not(x[0] in classes)):
            m = list()
            i = list()
            for i in models.storage.all().values():
                    m.append(i.__str__())
            print(i)
        else:
            print("class doesn't exist **")

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)"""
        list_str = args.split()
        if not list_str:
            print("** class name missing **")
        elif list_str[0] not in classes:
            print("** class doesn't exist **")
        elif len(list_str) == 1:
            print("** instance id missing **")
        elif len(list_str) == 2:
            print("** attribute name missing **")
        elif len(list_str) == 3:
            print("** value missing **")
        else:
            objects = models.storage.all()
            instance = "{}.{}".format(list_str[0], list_str[1])
            if instance in objects.keys():
                for value in objects.values():
                    try:
                        attr_type = type(getattr(value, list_str[2]))
                        list_str[3] = attr_type(list_str[3])
                    except AttributeError:
                        pass
                s = str(list_str[2])
                value.s = list_str[3]
                models.storage.save()
            else:
                print("** no instance found **")    

#HBNBCommand = HBNBCommand()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
