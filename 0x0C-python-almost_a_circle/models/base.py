#!/usr/bin/python3
""" This Module defines a class Base model """
import json
import os


class Base:
    """ A Base Class for all other classes """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialization """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ sterilizes a JSON object[list_dictionaries] to JSON string """
        if list_dictionaries is None:
            return "[]"
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation to a JSON file """

        filename = f"{cls.__name__}.json"
        if list_objs is None:
            list_dict = []
        else:
            list_dict = [obj.to_dictionary() for obj in list_objs]
        with open(filename, 'w') as fp:
            fp.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        json_string_list = []
        if json_string is not None and json_string != "":
            json_string_list = json.loads(json_string)
        return json_string_list

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
        elif cls.__name__ == "Square":
            obj = cls(1)
        obj.update(**dictionary)
        return (obj)

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = f"{cls.__name__}.json"
        obj_list = []

        if os.path.exists(filename):
            with open(filename) as fp:
                json_string = fp.read()
                dict_list = cls.from_json_string(json_string)
                for dic in dict_list:
                    obj_list.append(cls.create(**dic))
        return obj_list
