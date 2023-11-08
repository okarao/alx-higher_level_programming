#!/usr/bin/python3

def append_write(filename="", text=""):
    """
    Append a string to the end of a text file (UTF8) and return the number of characters added.

    :param filename: The name of the file to append to (default is an empty string).
    :param text: The string to append to the file (default is an empty string).
    :return: The number of characters added.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        chars_added = file.write(text)
    return chars_added
