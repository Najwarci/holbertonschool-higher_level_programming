#!/usr/bin/python3
"""Defines my square with private size, position, and print method"""


class Square:
    """Class that defines my square with a size and a position"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes square with optional size and position, and validates them"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Returns the current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with type and value verification"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Returns the current position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square with type and value verification"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with '#' considering its position"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
