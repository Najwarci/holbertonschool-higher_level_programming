#!/usr/bin/python3
"""Defines my square with private size and a method to compute"""


class Square:
    """Class that defines my square with a size"""

    def __init__(self, size=0):
        """Initializes square with optional size and validates it"""
        self.size = size  # utilise le setter pour valider

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
