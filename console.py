#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
import models

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    classes = ["BaseModel", "State", "City", "Amenity", "Place", "Review", "User"]
    def do_EOF(self, line):
        '''EOF to exit the program'''
        return True
    def do_quit(self, line):
        '''exit the application'''
        return True
    def emptyline(self):
        '''Doesn't do anything'''
        pass
    def do_create (self, line):
        if len(line) == 0:
            print("** class name missing **")
        elif line in self.classes:
            new_instance = eval(line + "()")
            new_instance.save()
            print(new_instance.id)
        else:
            print(" ** class doesn't exist **")
    def do_show (self, line):
        if len(line) is 0:
            print("** class name missing **")
        else:
            list_key = line.split()
            if len(list_key) < 2:
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
                    print("** class doesn't exist·**")

    def do_destroy(self, line):
        if len(line) is 0:
            print("** class name missing **")
        else:
            list_key = line.split()
            if len(list_key) < 2:
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
                    print("** class doesn't exist·**")

    def do_all(self, line):
        obj_dict = storage.all()
        list = []
        if len(line) == 0:
            for key in obj_dict:
                list.append(str(obj_dict[key]))
            if len(list) != 0:
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
        if len(line) is 0:
            print("** class name missing **")
        else:
            list_key = line.split()
            if len(list_key) < 2:
                print("** instance id missing **")
            else:
                if len(list_key) < 3:
                    print("** attribute name missing **")
                elif len(list_key) < 4:
                    print("** value missing **")
                else:
                    if list_key[0] in self.classes:
                        key = list_key[0] + "." + list_key[1]
                        new_object = storage.all()
                        if key in new_object:
                            get_att = getattr(new_object[key], list_key[2], "")
                            setattr(new_object[key], str(list_key[2]), list_key[3][1:-1])
                            new_object[key].save()
                        else:
                            print("** no instance found **")
                    else:
                        print("** class doesn't exist·**")
if __name__ == '__main__':
    HBNBCommand().cmdloop()
