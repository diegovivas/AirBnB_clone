#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:

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
    def reload(self):
        class_list = [BaseModel, User]
        try:
            otro = {}
            otro2 = {}
            with open(self.__file_path, "r") as f:
                otro = json.load(f)
            for key in otro:
                y = otro[key]["__class__"]
                for idx, item in enumerate(class_list):
                    if y in str(item):
                        a = class_list[idx](**otro[key])
                otro2.setdefault(key, a)
            self.__objects = otro2
        except:
            pass
