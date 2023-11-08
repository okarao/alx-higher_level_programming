#!/usr/bin/python3

def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8) and return the number of characters written.

    :param filename: The name of the file to write to (default is an empty string).
    :param text: The string to write to the file (default is an empty string).
    :return: The number of characters written.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        chars_written = file.write(text)
    return chars_written
