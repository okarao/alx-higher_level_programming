#!/usr/bin/python3
'''
Write class Rectagle that imports for BaseGeometry
'''


class BaseGeometry:
    """Base class BaseGeometry"""

    def area(self):
        """public instance method"""
        raise Exception("area() is not implemented")

    def integer_validation(self, name, value):
        """Validate value as a positive integer"""
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")


class Rectangle(BaseGeometry):
    """Class Rectangle inheriting from class BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a Rectangle instance with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.

        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

        def area(self):
            """Determine and return area of rectangle"""
            return (self.__widht * self.__height)

        def __str__(self):
            """Return a string representation of the rectangle."""
            return (f"[Rectangle] {self.__width}/{self.__height}")

        def __repr__(self):
            """Return a string representation of the rectangle"""
            return (f"Rectangle({self.__width}, {self.__height})")

class Square(Rectangle):
    """A square class that inherits from Rectangle class."""

    def __init__(self, size):
        """Initialization"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return (self.__size * self.__size)

    def __str__(self):
        """Return a string representation of the square."""
        return (f"[Square] {self.__size}/{self.__size}")
