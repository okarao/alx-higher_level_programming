#!/usr/bin/python3
"""Module containing a function that creates an Object from a “JSON file"""


import json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file

    Args:
        filename: JSON from which python object is created
    """
    with open(filename, encoding='utf-8') as my_file:
        json.load(my_file)
