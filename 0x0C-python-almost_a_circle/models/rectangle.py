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
        if self.y > 0:
            for mov in range(self.__y):
                print()
        for i in range(self.__height):
            if self.x is not 0:
                print(" " * self.x, end="")
            print('#' * self.width)

    def __str__(self):
        """overrinding __str__ method"""
        name = self.__class__.__name__
        return "[{}] ({}) {}/{} - {}/{}".format(
            name, self.id,
            self.x, self.y,
            self.width, self.height)

    def update(self, *args, **kwargs):
        """update the attributes"""
        if args and len(args) > 0:
            for idx, arg in enumerate(args):
                if idx == 0:
                    super().__init__(arg)
                elif idx == 1:
                    self.width = arg
                elif idx == 2:
                    self.height = arg
                elif idx == 3:
                    self.x = arg
                elif idx == 4:
                    self.y = arg
        elif kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'id':
                    super().__init__(value)
                if key == 'width':
                    self.width = value
                if key == 'height':
                    self.height = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value
