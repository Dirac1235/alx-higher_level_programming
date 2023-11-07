#!/usr/bin/python3
""" contains function that converts object to json string"""
import json


def save_to_json_file(my_obj, filename):
    """converts object to json string and saves to file"""
    json.dump(my_obj, filename)
