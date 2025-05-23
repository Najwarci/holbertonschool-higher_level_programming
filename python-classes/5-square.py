#!/usr/bin/python3
"""Defines my square with size, area and print method"""


class Square:
    """Class that defines my square with a size"""

    def __init__(self, size=0):
        """Initializes square with optional size and validates it"""
        self.size = size

    @property
    def size(self):
        """Gets the current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using '#' or prints empty line if size is 0"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
