#!/usr/bin/python3
"""Defines a class Rectangle with width and height validation."""


class Rectangle:
    """Represents a rectangle."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """Return the rectangle as a string of '#' characters."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_lines = ["#" * self.__width for _ in range(self.__height)]
        return "\n".join(rect_lines)

    def __repr__(self):
        """Return a string representation that can recreate the instance."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message when an instance is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
