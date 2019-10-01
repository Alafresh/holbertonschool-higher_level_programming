#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        if not isinstance(size,(int)):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        count = 1
        if self.__size is 0:
            print()
        for i in range(self.__size):
            print()
            for j in range(self.__size):
                print('{}'.format('#'), end='')
