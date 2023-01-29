#!/usr/bin/python3
"""Rectangle Class"""

from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""

    @property
    def width(self):
        return self.__width or 0

    @width.setter
    def width(self, value):
        self.__width = Base.check_int(value, "width")

    @property
    def height(self):
        return self.__height or 0

    @height.setter
    def height(self, value):
        self.__height = Base.check_int(value, "height")

    @property
    def x(self):
        return self.__x or 0

    @x.setter
    def x(self, value):
        self.__x = Base.check_int(value, "x", 0)

    @property
    def y(self):
        return self.__y or 0

    @y.setter
    def y(self, value):
        self.__y = Base.check_int(value, "y", 0)

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
