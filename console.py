#!/usr/bin/python3
"""
This module will be the console for manage
all classes in this project
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
import models


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand
    """
    prompt = '(hbnb) '
    classes = ["BaseModel", "State", "City",
               "Amenity", "Place", "Review", "User"]

    def do_EOF(self, line):
        '''EOF to exit the program'''
        return True

    def do_quit(self, line):
        '''exit the application'''
        return True

    def emptyline(self):
        '''Doesn't do anything'''
        pass

    def do_create(self, line):
        '''do_create function create new object '''
        if len(line) == 0:
            print("** class name missing **")
        elif line in self.classes:
            new_instance = eval(line + "()")
            new_instance.save()
            print(new_instance.id)
        else:
            print(" ** class doesn't exist **")

    def do_show(self, line):
        ''' do_show show selectec object'''
        if len(line) is 0:
            print("** class name missing **")
        else:
            list_key = line.split()
            if len(list_key) < 2:
                if list_key[0] not in self.classes:
                    print("** class doesn't exist **")
                else:
                    print("** instance id missing **")
            else:
                if list_key[0] in self.classes:
                    key = list_key[0] + "." + list_key[1]
                    new_object = storage.all()
                    if key in new_object:
                        print(new_object[key])
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")

    def do_destroy(self, line):
        ''' do_destroy'''
        if len(line) is 0:
            print("** class name missing **")
        else:
            list_key = line.split()
            if len(list_key) < 2:
                if list_key[0] not in self.classes:
                    print("** class doesn't exist **")
                else:
                    print("** instance id missing **")
            else:
                if list_key[0] in self.classes:
                    key = list_key[0] + "." + list_key[1]
                    new_object = storage.all()
                    if key in new_object:
                        del new_object[key]
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")

    def do_all(self, line):
        ''' do_all '''
        obj_dict = storage.all()
        list = []
        if len(line) == 0:
            for key in obj_dict:
                list.append(str(obj_dict[key]))
            print(list)
        else:
            for key in obj_dict:
                class_split = key.split(".")
                if class_split[0] == line:
                    list.append(str(obj_dict[key]))
            if len(list) == 0:
                print("** class doesn't exist **")
            else:
                print(list)

    def do_update(self, line):
        ''' do_update'''
        if len(line) is 0:
            print("** class name missing **")
        else:
            line = line.replace('"', '')
            line = line.replace("'", "")
            list_key = line.split()
            if list_key[0] not in self.classes:
                print("** class doesn't exist **")
                return
            if len(list_key) < 2:
                print("** instance id missing **")
            else:
                if len(list_key) < 3:
                    new_object = storage.all()
                    key = list_key[0] + "." + list_key[1]
                    if key not in new_object:
                        print("** no instance found **")
                    else:
                        print("** attribute name missing **")
                elif len(list_key) < 4:
                    print("** value missing **")
                else:
                    if list_key[0] in self.classes:
                        key = list_key[0] + "." + list_key[1]
                        new_object = storage.all()
                        if key in new_object:
                            tipo = type(new_object[key])
                            padre = tipo.__dict__.copy()
                            if list_key[2] in padre:
                                tipo2 = type(padre[list_key[2]])
                                list_key[3] = tipo2(list_key[3])
                            else:
                                try:
                                    list_key[3] = eval(list_key[3])
                                except:
                                    pass
                            setattr(new_object[key], list_key[2], list_key[3])
                            new_object[key].save()
                        else:
                            print("** no instance found **")

    def default(self, line):
        '''default '''
        num_of_instances = 0
        list_key = line.split(".")
        if len(list_key) > 1:
            args = "." + list_key[1]
        list_arg = line.split('"')
        num_args = len(list_arg)
        if len(list_key) > 1:
            if args == '.all()' and list_key[0] in self.classes:
                self.do_all(list_key[0])
            elif args == '.count()' and list_key[0] in self.classes:
                for key in models.storage.all():
                    if list_key[0] in key:
                        num_of_instances += 1
                print(num_of_instances)
            elif 'show' in line:
                if len(list_arg) == 1:
                    print("** instance id missing **")
                else:
                    self.do_show(list_arg[0][:-6] + ' ' + list_arg[1])
            elif 'destroy' in line:
                if len(list_arg) == 1:
                    print("** instance id missing **")
                else:
                    self.do_destroy(list_arg[0][:-9] + ' ' + list_arg[1])
            elif 'update' in line:
                line_dict = line.split("{")
                if len(line_dict) == 2:
                    our_dict = "{" + line_dict[1][:-1]
                    dict_final = eval(our_dict)
                    command = list_arg[0][:-8] + ' '
                    command += list_arg[1] + ' '
                    command_f = command
                    for key in dict_final:
                        command += str(key) + ' '
                        command += str(dict_final[key])
                        self.do_update(command)
                        command = command_f
                else:
                    if num_args == 1:
                        print("** instance id missing **")
                    elif num_args == 2 or num_args == 3:
                        print("** attribute name missing **")
                    elif num_args == 4:
                        print("** value missing **")
                    elif num_args >= 5:
                        command = list_arg[0][:-8] + ' '
                        command += list_arg[1] + ' '
                        command += list_arg[3] + ' '
                        try:
                            command += list_arg[5]
                        except:
                            list_arg[4] = list_arg[4][:-1]
                            command += list_arg[4].replace(",", "")
                        self.do_update(command)
            else:
                print("*** Unknown syntax: {}".format(line))
        else:
            print("*** Unknown syntax: {}".format(line))
if __name__ == '__main__':
    HBNBCommand().cmdloop()
