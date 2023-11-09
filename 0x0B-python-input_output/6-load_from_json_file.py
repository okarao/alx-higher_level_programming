#!/usr/bin/python3
"""Module containing a function that creates an Object from a “JSON file"""


import json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file

    Args:
        filename: JSON from which python object is created
    Returns:
        Python object
    """
    with open(filename, encoding='utf-8') as my_file:
        return json.load(my_file)
