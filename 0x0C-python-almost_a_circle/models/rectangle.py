#!/usr/bin/python3
'''Module for class Rectangle'''
from models.base import Base


class Rectangle(Base):
    '''Class Rectangle inherits from Base'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Class construct'''
        super().__init__(id)
        __width = width
        __height = height
        __x = x
        __y = y
