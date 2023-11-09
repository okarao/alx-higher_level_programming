#!/usr/bin/python3
"""Module containing a function that creates an Object from a “JSON file"""


import json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file

    Args:
        filename: JSON from which python object is created
    """
    with open(filename, 'r', encoding='utf-8') as my_file:
        json.load(filename, my_file)
