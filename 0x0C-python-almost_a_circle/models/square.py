#!/usr/bin/python3
"""Import module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Base Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor initialize"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overloading"""
        name = self.__class__.__name__
        return "[{}] ({}) {}/{} - {}".format(
                name, self.id,
                self.x, self.y,
                self.width)

    @property
    def size(self):
        """getter of size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter of size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update the attributes"""
        if len(args) > 0 and args is not None:
            att = ["id", "size", "x", "y"]
            count = 0
            for attr in args:
                setattr(self, att[count], args[count])
                count = count + 1
        elif len(kwargs) > 0 and kwargs is not None:
            for ky, vle in kwargs.items():
                setattr(self, ky, vle)

    def to_dictionary(self):
        dictionary = {
                    'id': self.id, 'size': self.size,
                    'x': self.x, 'y': self.y}
        return dictionary
