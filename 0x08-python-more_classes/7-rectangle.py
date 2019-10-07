#!/usr/bin/python3
class Rectangle:

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif self.__width < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif self.__height < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height is 0 or self.__width is 0:
            return 0
        return (self.__width + self.__width) + (self.__height + self.__height)

    def __str__(self):
        rect = ""
        count = 0
        if self.__width is 0 or self.__height is 0:
            return rectangle
        for i in range(self.__height):
            for j in range(self.__width):
                rect += str(self.print_symbol)
            if count is self.__height - 1:
                return rect
            rect += "\n"
            count += 1
        return rect

    def __repr__(self):
        return "Rectangle ({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print('Bye rectangle...')
        type(self).number_of_instances -= 1
