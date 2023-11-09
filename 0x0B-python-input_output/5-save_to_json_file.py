#!/usr/bin/python3
"""Module containing a function that writes an Object to a text file, using a JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation

    Args:
        my_obj: JSON object
        filemane: The containing the JSON representation of the object
    """
    with open(filename, 'w', encoding='utf-8') as my_file:
        json.dumps(my_obj, my_file)
