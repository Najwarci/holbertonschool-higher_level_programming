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

    splitters = ['.', '?', ':']
    new_text = ""
    i = 0

    while i < len(text):
        new_text += text[i]
        if text[i] in splitters:
            new_text += "\n\n"
            i += 1
            # Skip following spaces
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1

    lines = new_text.split('\n')
    for line in lines:
        print(line.strip())
