#!/usr/bin/python3
'''Create a class BaseGeometry based on 6-base_geometry'''


class BaseGeometry:
    """
    Class BaseGeometry based on 6-base_geometry.py

    """

    def area(self):
        """
        Public instance method area

        Raises:
            Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates value.

        Args:
            name: a string
            value: an integer 

        Raises:
            TypeError: if value is not integer
            ValueError: if value is less than 0

        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0">
