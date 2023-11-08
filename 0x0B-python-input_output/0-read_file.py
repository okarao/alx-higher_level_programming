#!/usr/bin/python3

def read_file(filename=""):
    """
    Read a text file (UTF8) and print its content to stdout.

    :param filename: The name of the file to read (default is an empty string).
    """
    with open(filename, encoding='utf-8') as file:
        content = file.read()
        print(content)
