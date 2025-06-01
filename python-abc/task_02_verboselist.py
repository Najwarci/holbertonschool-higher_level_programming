#!/usr/bin/env python3
"""
Module that defines the VerboseList class, which extends the built-in list
with custom notifications on modifications.
"""


class VerboseList(list):
    """
    A custom list that prints messages when items are added or removed.
    """

    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        item = self[index]  # Will raise IndexError if invalid
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
