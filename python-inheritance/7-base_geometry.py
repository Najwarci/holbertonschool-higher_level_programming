#!/usr/bin/python3
"""
Defines class BaseGeometry for geometric shapes
"""


class BaseGeometry:
    """
    Base class for geometry
    """

    def area(self):
        """
        Raise an exception (not implemented)
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that value is a positive integer

        Args:
            name (str): name of the value
            value (int): value to validate

        Raises:
            TypeError: if value is not int
            ValueError: if value <= 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
