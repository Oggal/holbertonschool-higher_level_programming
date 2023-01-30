#!/usr/bin/python3
""" Base Class"""
import json


class Base():
    """Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
        self.id = Base.__nb_objects if id is None else id

    def check_int(value, val_name, min=None):
        """check if an int value is valid, raise error if not """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(val_name))
        if min is None:
            if value <= 0:
                raise ValueError("{} must be > 0".format(val_name))
        else:
            if value < min:
                raise ValueError("{} must be >= {}".format(val_name, min))
        return value

    def to_json_string(list_dictionaries=[]):
        """get JSON strings"""
        list_dictionaries = list_dictionaries or []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = str(cls.__name__) + ".json"

        with open(filename, "w") as file:
            file.write(
                    Base.to_json_string(
                        [obj.to_dictionary() for obj in list_objs]))
