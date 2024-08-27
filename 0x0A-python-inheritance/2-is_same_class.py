#!/usr/bin/python3
'''Defines a function that returns true 
if the object is exactly an instance of the specified class
'''

def is_same_class(obj, a_class):
    """
    is_same_class - determine is object is instance of class

    Args:
        obj: object
        a_class: the class
    
    Returns:
        True if object is exactly instance of class or false
    """
    return (type(obj) == a_class)
