#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    def do_EOF(self, line):
        '''EOF to exit the program'''
        return True
    def do_quit(self, line):
        '''exit the application'''
        return True
    def emptyline(self):
        '''Doesn't do anything'''
        pass
if __name__ == '__main__':
    HBNBCommand().cmdloop()
