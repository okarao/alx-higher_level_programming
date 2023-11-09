#!/usr/bin/python3
""""Module containing  a function that returns an object (Python data structure) represented by a JSON string"""

import json

def from_json_string(my_str):
    """
    This module JSON string and returns an equivalent string object

    Args:
        my_str: JSON string to be converted

    Returns:
        String Object
    """
    str_obj = json.load(my_str)
    return(str_obj)
