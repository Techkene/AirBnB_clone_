#!/usr/bin/python3
""" Console Module """
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """ Contain the functionality for the HBNB console """
    " ----- CLI basic functionality ----- "

    prompt = '(hbnb) '

    def do_EOF(sels, arg):
        """ Handles EOF """
        return True
    def do_quit(self, arg):
        """ [quit + ENTER]: cmd exits the CLI """
        return True

    def emptyline(self):
        """ Handles [empty line + ENTER] """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
