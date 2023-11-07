#!/usr/bin/python3
""" contains function that jsonify file"""
import json


def to_json_string(my_obj):
    """converts string to json representation"""
    return json.dumps(my_obj)
