#!/usr/bin/python3
''' 
Write class Rectagle that imports for BaseGeometry
'''


from 7-base_geometry import BaseGeometry


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
