#!/usr/bin/python3
''' Defines a function that returns True if the object is an instance of
or if the object is an instance of a class that inherited from,
the specified class otherwise False'''


def is_kind_of_class(obj, a_class):
    """Determines wheather the object is an instance of
    or if the object is an instnance of a that inherited from
    the specified class
    """
    return (isinstance(obj, a_class))
