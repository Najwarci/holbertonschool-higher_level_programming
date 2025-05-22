#!/usr/bin/python3
"""Defines my square with private size and validation"""


class Square:
    """Class that defines my square with a size"""

    def __init__(self, size=0):
        """Initializes square with optional size and validates it"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
