#!/usr/bin/python3
"""Square Class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        parts = [type(self).__name__, self.id, self.x,
                 self.y, self.size]
        res = "[{0}] ({1}) {2}/{3} - {4}".format(*parts)
        return res

    def update(self, *args, **kwargs):
        """Update the Square"""
        if args == () and kwargs is not None:
            nargs = [kwargs.get("id"), kwargs.get("size"), kwargs.get("size"),
                     kwargs.get("x"), kwargs.get("y")]
        nargs = []
        try:
            nargs[0] = args[0]
            nargs[1] = args[1]
            nargs[2] = args[1]
            nargs[3] = args[2]
            nargs[4] = args[3]
        except IndexError:
            pass
        super().update(*nargs)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
