#!/usr/bin/python3
'''Beam me the file scotty!'''


class Student():
    """Student Data Class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get json rep"""
        if attrs is None:
            return self.__dict__
        else:
            return {
                k: v for k, v in self.__dict__.items() if k in attrs}
