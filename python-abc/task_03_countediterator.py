#!/usr/bin/env python3
"""
Module that defines CountedIterator to keep track
of the number of items iterated.
"""


class CountedIterator:
    """
    An iterator that counts how many items have been retrieved.
    """

    def __init__(self, iterable):
        self._iterator = iter(iterable)
        self._count = 0

    def __next__(self):
        item = next(self._iterator)  # Raises StopIteration if needed
        self._count += 1
        return item

    def __iter__(self):
        return self

    def get_count(self):
        """
        Return the number of items that have been iterated so far.
        """
        return self._count
