#!/usr/bin/python3
"""Module containing a function that appends a string at the end of a text file and returns the number of characters added"""



def append_write(filename="", text=""):
    """
    Append a string to the end of a text file (UTF8) and return the number of characters added.

    Args:
        filename(str, optional): The name of the file to append to (default is an empty string).
        text(str, optional): The string to append to the file (default is an empty string).
    Returns:
        int: The number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        chars_added = file.write(text)
    return chars_added
