#!/usr/bin/python3
"""
the console command line program
"""
import cmd
from models.base_model import BaseModel
from models import storage
from shlex import split
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    class inheriting from the cmd module
    """
    ValidClass = ["BaseModel", "User"]

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
            new_instance = eval(command[0]())
            storage.save()
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
                print(objects[key])
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

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.
        Ex: $ all BaseModel or $ all.
        """
        command = split(arg)
        objects = storage.all()

        if len(command) == 0:
            for key, value in objects.items():
                print(str(value))
        elif command[0] not in self.ValidClass:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                class_name = key.split('.')
                if class_name[0] == command[0]:
                    print(str(value))

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
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
                attribute_name = command[2]
                attribute_value = command[3]

                try:
                    attribute_value = eval(attribute_name)
                except Exception:
                    pass
                setattr(obj, attribute_name, attribute_value)
                obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
