#!/usr/bin/python3
""" Console Module """
import cmd
import sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.__init__ import storage


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

    def help_quit(self):
        """ Method to exit the HBNB console """
        exit()

    def help_EOF(self arg):
        """ Print the help documentation for EOF """
        print("Exits the program without formatting\n")

    def do_create:
        """ Create an object of any class"""
        if not args:
            print("** class name missing **")
            return
        elif args not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes[args]()
        storage.save()
        print(new_instance.id)
        storage.save()

    def help_create(self):
        """ Help information for the create method """
        print("create a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        """ Method to show an individual object """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]
        # guard against trailing args
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBHBCommand.classes:
            print("** class doesn't exist **")
            return

        key = c_name + "." + c_id
        try:
            print(storage._FileStorage__objects[key])
        except KeyError:
            print("** no instance found **")

    def help_show(self):
        """ Help information for the show command """
        print("Shows an individual instance of a class")
        print("[Usage]: shwo <className> <objectID>\n")

    def do_destroy(self, arg):
        """ Deletes instances based on cls name and instance id, save
            change Command syntax: destroy + [cls name] + [id]
        """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classses:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id

        try:
            del(storage.all()[key])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def help_destroy(self):
        """ Help information for the destroy command """
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectID>\n")

    def do_all(self, arg):
        """ Print strings representaion of all instances based on cls name
            Command syntax: all + [ENTER]
        """
        print_list = []

        if args:
            args = args.split(' ')[0]  # remove possible trailing args"
            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for k, v in storage._FileStorage__objects.item():
                if k.split('.')[0] == args:
                    print_list.append(str(v))
        else:
            for k, v in storage.Filestorage__object.items():
                print_list.append(str(v))

        print(print_list)

    def help_all(self):
        """ Help information for the all command """
        print("Shows all objects, or all of a class")
        print("[usage]: all <className>\n")

    def do_update(self, args):
        """ Updates a certain object with new info """
        c_name = c_id = att_val = kwargs = ''
        # isolate cls from id/args, ex: (<cls>, delim, <id/arrgs>)
        args = args.partition(" ")
        if args[0]:
            c_name = args[0]
        else:  # class name not present
            print("** class name missing **")
            return
        # isolate id from args
        args = args[2].partition(" ")
        if args[0]:
            c_id = args[0]
        else:  # id not present
            print("** instance id missing **")
            return
        # generate key from class and id
        key = c_name + "." + c_id
        # determine if key is present
        if key not in storage.al():
            print("**  no instance found **")
            return
        # first determine if kwargs or args
        if '{' in args[2] and '}' in args[2] and type(eval(args[2])) is dict:
            kwargs = eval(args[2])
            args = []  # reformat kwargs into list, ex: [<name>, <value>,...]
            for k, v in kwags.item():
                args.append(k)
                args.append(v)


if __name__ == '__main__':
    """ Loops the CLI, prevents running on import  """
    HBNBCommand().cmdloop()
