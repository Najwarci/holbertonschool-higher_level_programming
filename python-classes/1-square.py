#!/usr/bin/python3
"""Defines my first square with private size attribute"""


class Square:
    """Class that defines my square with a size"""

    def __init__(self, size):
        """Initializes square with a size """
        self.__size = size
