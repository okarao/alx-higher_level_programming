#!/usr/bin/python3
"""Module containing the function write_file"""



def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8) and return the number of characters written.

    Args:
        filename(str, optional): The name of the file to write to (default is an empty string).
        text(str, optional): The string to write to the file (default is an empty string).
    Returns:
        int: number of characters written.
    """
    with open(filename,'w', encoding='utf-8') as file:
        chars_written = file.write(text)
    return chars_written
