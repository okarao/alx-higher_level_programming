#!/usr/bin/python3
'''
Defines a function that returns the list of attributes and methos
of an object
'''

def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.
    

    Args:
        obj: The object

    Returns:
        A list of string representation of attributes and methods

    """
    return (dir(obj))
