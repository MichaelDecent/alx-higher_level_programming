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
        if cls.__name__ == 'Rectangle':
            dummy_inst = cls(1, 1)
        elif cls.__name__ == 'Square':
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
                if cls.__name__ == "Rectangle":
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == "Square":
                    fieldnames = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Serializes list_objs and saves to file"""

        file_name = f"{cls.__name__}.csv"
        list_inst = []
        try:
            with open(file_name, 'r') as csv_file:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csv_file, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items(
                    ))for d in list_dicts]
        except FileNotFoundError:
            return []
        for dic in list_dicts:
            list_inst.append(cls.create(**dic))
        return list_inst

     @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
