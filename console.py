#!/usr/bin/python3
"""
the console command line program
"""
import cmd
from models.base_model import BaseModel
from models import storage
from shlex import split
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    class inheriting from the cmd module
    """
    ValidClass = ["BaseModel",
                  "User",
                  "State",
                  "City",
                  "Place",
                  "Amenity",
                  "Review"]

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        command to quit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF to quit the program
        """
        return True

    def emptyline(self):
        """
        an empty line + ENTER should not execute anything
        """
        pass

    def do_create(self, arg):
        """
        this command Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        Ex: $ create BaseModel
        If the class name is missing,
        print ** class name missing ** (ex: $ create)
        If the class name does not exist,
        print ** class doesn't exist ** (ex: $ create MyModel)
        """
        command = split(arg)
        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in self.ValidClass:
            print("** class doesn't exist **")
        else:
            new_instance = eval(f"{command[0]}()")
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        command = split(arg)

        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in self.ValidClass:
            print("** class doesn't exist **")
        elif len(command) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = "{}.{}".format(command[0], command[1])
            if key in objects:
                print(str(objects[key]))
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        command = split(arg)

        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in self.ValidClass:
            print("** class doesn't exist **")
        elif len(command) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(command[0], command[1])
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_delete_all(self, arg):
        objects = storage.all()
        command = split(arg)

        if len(command) == 0:
            for key in list(objects.keys()):
                del objects[key]
                storage.save()
        elif command[0] not in self.ValidClass:
            print("** class doesn't exist **")
        else:
            for key in list(objects.keys()):
                if key.split('.')[0] == command[0]:
                    del objects[key]
                    storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.
        Ex: $ all BaseModel or $ all.
        """
        objects = storage.all()
        command = split(arg)

        if len(command) == 0:
            for key, value in objects.items():
                print(str(value))
        elif command[0] not in self.ValidClass:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split('.')[0] == command[0]:
                    print(str(value))

    def do_update(self, arg):
        """
         Updates an instance based on the class name and id
         by adding or updating attribute
         (save the change into the JSON file).
         Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        command = split(arg)

        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in self.ValidClass:
            print("** class doesn't exist **")
        elif len(command) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(command[0], command[1])
            if key not in objects:
                print("** no instance found **")
            elif len(command) < 3:
                print("** attribute name missing **")
            elif len(command) < 4:
                print("** value missing **")
            else:
                obj = objects[key]
                attr_name = command[2]
                attr_value = command[3]

                try:
                    attr_value = eval(attr_value)
                except Exception:
                    pass

                setattr(obj, attr_name, attr_value)
                obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
