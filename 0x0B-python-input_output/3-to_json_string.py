#!/usr/bin/python3
"""Module containing a function that returns the JSON representation of an object (string)"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string)

    Args:
        my_object(type): The Object to be serialized to JSON

    Returns:
        str: JSON representation of the Object
    """
    return json.dumps(my_obj)
