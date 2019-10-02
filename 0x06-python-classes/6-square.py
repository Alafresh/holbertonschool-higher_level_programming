#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, (int)):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        if position < (0, 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__size = size
        self.__position = position

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
        else:
            for i in range(self.__size):
                if self.__position[1] > 0:
                    pass
                print(' ' * self.__position[0], end='')
                for j in range(self.__size):
                    print("#", end='')
                print()

    def position(self):
        return self.__position

    def position(self, value):
        if type(value) != tuple or type(value[0]) != int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] < 0 or value[1] < 0 or type(value[1]) != int:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value
