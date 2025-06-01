#!/usr/bin/env python3
"""
Defines an abstract class Shape and its implementations: Circle and Rectangle,
and demonstrates duck typing with a shape_info function.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for geometric shapes.
    """

    @abstractmethod
    def area(self):
        """
        Compute the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Compute the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Circle class implementing Shape interface.
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle class implementing Shape interface.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of any object that implements
    area() and perimeter() methods (duck typing).
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
