#!/usr/bin/python3
"""
Function that prints a text with 2 new lines after each
'.', '?' and ':' character.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?' and ':'.

    Args:
        text (str): The text to be formatted.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ['.', '?', ':']:
            print("\n")
            i += 1
            # Skip all spaces after the punctuation
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
