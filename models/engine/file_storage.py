#!/usr/bin/python3
import json 

class FileStorage():

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        stri = obj.__class__.__name__
        stri = stri + "." + obj.id
        self.__objects.setdefault(stri, obj)

    def save(self):
        otro = {}
        for key in self.__objects:
            otro.setdefault(key, self.__objects[key].to_dict())
        jdic = json.dumps(otro)
        with open(self.__file_path, "w") as f:
            f.write(jdic)
        print(otro)
    def reload(self):
        try:
            otro = {}
            with open(self.__file_path, "r") as f:
                otro = json.load(f)
        except:
            pass
