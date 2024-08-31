#!/usr/bin/python3
"""
Defines a class BaseGeometry based on 6-base_geometry

"""


class BaseGeometry:
    """
    Class BaseGeometry based on 6-base_geometry
    """

    def area(self):
        """
        public instance method 
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is a positive integer.
        """
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
