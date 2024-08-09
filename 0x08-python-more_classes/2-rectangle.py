#!/usr/bin/python3
'''
This module defines a class Rectangle based on (1-rectangle.py)
'''


class Rectangle:
    """ The class can create instances taking two Arguments

    Args:
        width (int): The width of the rectangle, default value is 0
        height (int): the height of the rectangle, default value is 0

    """
    def __init__(self, width=0, height=0):
        # use setters to assign
        self.width = width
        self.height = height

    @property
    def width(self):
        """__width getter.

        Returns:
            __width (int): horizontal dimenstion of the rectangle

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Args:
            value (int): horizontal dimension of rectangle

        Attribute:
            __width (int): horizontal dimension of rectangle
        Raises:
            TypeError: if `value` is not integer
            ValueError: if `value` is less than 0

        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """__height getter.

        Returns:
            __height (int): vertical dimension of rectangle

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Args:
            value (int): vertical dimension of a rectangle

        Attributes:
            __height (int): vertical dimension of a rectangle

        Raises:
            TypeError: if `value` is not an integer
            ValueError: if `value` is less than 0

        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('Height must be greater or equal to 0')
        self.__height = value

    def area(self):
        """Calculate the area of a rectangle

        Returns:
            The area of a rectangle

        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of a rectangle
        Returns:
            0 or perimeter of the rectangle

        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
