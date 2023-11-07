#!/usr/bin/python3
""" contains from json string to object converter function"""
import json


def load_from_json_file(filename):
    """converts json string from file and converts to python object"""
    with open(filename, "r", encoding="utf-8") as file:
        object = json.load(file)
    return object
