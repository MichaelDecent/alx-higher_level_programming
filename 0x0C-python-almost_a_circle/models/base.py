#!/usr/bin/python3
""" This Module contain the Base Class """
import json
import csv


class Base:
    """ the base for all other classes """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialization """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file
            Args:
                list_obj:list of instances who inherits of Base
        """
        filename = f"{cls.__name__}.json"
        with open(filename, 'w') as f:
            if list_objs is None or len(list_objs) == 0:
                f.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(list_dict))

    @staticmethod            
    def from_json_string(json_string):
        """  returns the list of the JSON string representation json_string
            Agrs:
                json_string: a string representing a list of dictionaries
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """  returns an instance with all attributes already set """
        if cls.__name__ is 'Rectangle':
            dummy_inst = cls(1, 1)
        elif cls.__name__ is 'Square':
            dummy_inst = cls(1)

        dummy_inst.update(**dictionary)
        return dummy_inst

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        list_dict = []
        list_inst = []
        file_name = f"{cls.__name__}.json"
        try:
            with open(file_name) as f:
                file_str = f.read()
        except FileNotFoundError:
                return []

        list_dict = cls.from_json_string(file_str)
        for dic in list_dict:
            list_inst.append(cls.create(**dic))
        return (list_inst)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes list_objs and saves to file"""

        file_name = f"{cls.__name__}.csv"
        with open(file_name, "w", newline="") as csv_file:
            if list_objs is None or len(list_objs) == 0:
                csv.write("[]")
            else:
                if cls.__name__ == "Rectangle"
                    filename = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == "Square"
                    filename = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(csv_file)
                for obj in list_objs:
                    writer.writerow(obj)
