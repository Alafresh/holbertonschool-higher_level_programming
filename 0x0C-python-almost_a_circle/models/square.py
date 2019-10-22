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
