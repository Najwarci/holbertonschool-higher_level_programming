#!/usr/bin/python3
"""
Writes text to a file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file and returns how many characters were written.

    Args:
        filename (str): File name.
        text (str): Text to write.

    Returns:
        int: Number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
