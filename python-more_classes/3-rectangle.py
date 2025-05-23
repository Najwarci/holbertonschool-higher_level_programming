#!/usr/bin/python3
"""Rectangle class definition."""


class Rectangle:
    """Defines a rectangle."""

    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property to retrieve width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter to set width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Property to retrieve height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Property setter to set height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter, or 0 if width or height is 0."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns the rectangle as a string of '#' characters."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = []
        for _ in range(self.__height):
            rect.append("#" * self.__width)
        return "\n".join(rect)

    def __repr__(self):
        """Returns a recreatable string representation."""
        return f"Rectangle({self.__width}, {self.__height})"
