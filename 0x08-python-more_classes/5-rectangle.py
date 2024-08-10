#!/usr/bin/python3
'''Defines a class Rectangle based on 4-rectangle.py

'''


class Rectangle:
    """Create private instance attributes taking two arquments

    Args:
        width (int): the horizontal dimension of the rectangle, default value 0
        height (int): the vertical dimension of the rectangle, default value 0

    """
    def __init__(self, width=0, height=0):
        # initialization
        self.width = width
        self.height = height

    @property
    def width(self):
        """__width getter.

        Returns:
            __width (int): horizontal dimension of rectangle

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

    @width.setter
    def height(self, value):
        """Args:
            value (int): vertical dimension of rectangle

        Attribute:
            __height (int): vertical dimension of rectangle

        Raises:
            TypeError: if `value` is not integer
            ValueError: if `value` is less than 0

        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Calculate the area of the rectangle

        Returns:
            area (int): width * height

        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of the rectangle

        Returns:
            0 or perimeter

        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle using #

        Returns:
            String rep of rectangle using # or empty string

        """
        if self.width == 0 or self.__height == 0:
            return ""

        total = ""
        for i in range(self.__height):
            total += "#" * self.__width
            if i < self.__height - 1:
                total += "\n"

        return total

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
