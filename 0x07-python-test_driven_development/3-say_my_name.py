#!/usr/bin/python3
# 3-say_my_name.py
''' Define say_my_name that prints my name is'''

def say_my_name(first_name, last_name=""):
    '''checks if the both first_name and last_name are strings
    otherwise raise a TypeError'''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

