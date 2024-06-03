#!/usr/bin/python3
import cmd
"""
the console command line program
"""


class HBNBCommand(cmd.Cmd):
    """
    class inheriting from the cmd module
    """

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
