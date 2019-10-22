#!/usr/bin/python3
from models.base import Base
"""Base Module"""


class Rectangle(Base):
    """Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """method to build rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of the width"""
        self.__width = value

    @property
    def height(self):
        """getter of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of the height"""
        self.__height = value

    @property
    def x(self):
        """getter of the x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter of the x"""
        self.__x = value

    @property
    def y(self):
        """getter of the y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter of the y"""
        self.__y = value
