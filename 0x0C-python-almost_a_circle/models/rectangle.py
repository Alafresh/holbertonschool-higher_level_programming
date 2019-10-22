#!/usr/bin/python3
"""Base Module"""
from models.base import Base


class Rectangle(Base):
    """Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """method to build rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of the width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """getter of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of the height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """getter of the x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter of the x"""
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """getter of the y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter of the y"""
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """method that calculate the area"""
        return self.__width * self.__height

    def display(self):
        """method to print rectangle"""
        for i in range(self.__height):
            for j in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        name = self.__class__.__name__
        return "[{}] ({}) {}/{} - {}/{}".format(
            name, self.id,
            self.x, self.y,
            self.width, self.height)
