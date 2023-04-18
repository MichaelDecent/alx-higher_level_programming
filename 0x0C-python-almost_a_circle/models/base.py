#!/usr/bin/python3
""" This Module defines a class Base model """
import json
import os


class Base:
    """ A Base Class for all other classes """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialization """
        if id is not None:
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize in CSV and save to a file"""
        my_file = cls.__name__ + ".csv"

        with open(my_file, 'w', newline='') as f:
            writer = csv.writer(f)

            for obj in list_objs:
                if cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])
                if cls.__name__ == "Rectangle":
                    writer.writerow(
                            [obj.id, obj.width, obj.height, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize in CSV"""
        obj_arr = []
        my_file = cls.__name__ + ".csv"

        with open(my_file, 'r', newline='') as f:
            reader = csv.reader(f)

            for row in reader:
                if cls.__name__ == "Square":
                    obj = {
                            "id": int(row[0]),
                            "size": int(row[1]),
                            "x": int(row[2]),
                            "y": int(row[3])
                            }
                if cls.__name__ == "Rectangle":
                    obj = {
                            "id": int(row[0]),
                            "width": int(row[1]),
                            "height": int(row[2]),
                            "x": int(row[3]),
                            "y": int(row[4])
                            }
                obj_arr.append(cls.create(**obj))

        return obj_arr

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw the rectangle and the square using turtle module
        Args:
            list_rectangle: List of rectangle objects
            list_squares: List of square objects
        """
        tur = turtle.Turtle()
        tur.screen.bgcolor("#b6578f")
        tur.pensize(2)
        tur.shape("square")

        tur.color("#ffffff")
        for rec in list_rectangles:
            tur.showturtle()
            tur.up()
            tur.goto(rec.x, rec.y)
            tur.down()
            for i in range(2):
                tur.forward(rec.width)
                tur.left(90)
                tur.forward(rec.height)
                tur.left(90)
            tur.hideturtle()
            tur.color("#e8543f")

        for sqr in list_squares:
            tur.showturtle()
            tur.up()
            tur.goto(sqr.x, sqr.y)
            tur.down()
            for i in range(2):
                tur.forward(sqr.width)
                tur.left(90)
                tur.forward(sqr.height)
                tur.left(90)
            tur.hideturtle()

        turtle.exitonclick()
