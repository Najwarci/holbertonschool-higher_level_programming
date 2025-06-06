#!/usr/bin/python3
"""
Defines Rectangle class that inherits from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class
    """

    def __init__(self, width, height):
        """
        Initialize rectangle with validated width and height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Return string representation of the rectangle
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
