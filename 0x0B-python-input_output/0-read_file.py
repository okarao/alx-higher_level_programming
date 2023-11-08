#!/usr/bin/python3
"""Module containing the function read file"""


def read_file(filename=""):
    """
    Read a text file (UTF8) and print its content to stdout.

    Args:
        filename(str, optional): The name of the file to read (default is an empty string).
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content, end='')
