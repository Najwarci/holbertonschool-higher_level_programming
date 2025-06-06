#!/usr/bin/python3
"""
Defines Square class that inherits from Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class
    """

    def __init__(self, size):
        """
        Initialize square with validated size
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Return area of the square
        """
        return self.__size * self.__size
