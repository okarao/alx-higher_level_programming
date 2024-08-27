#!/usr/bin/python3
'''
Defines a function that returns true if the object is an instance of a class
that inherited from the specified class
'''


def inherits_from(obj, a_class):
    """
    Determines if the object is an instance of a class that
    inherited from the specified class

    Args:
        obj: the object
        a_class: the specified class
    Returns:
        True or False
    """
    return (isinstance(obj, a_class) and type(obj) is not a_class)
