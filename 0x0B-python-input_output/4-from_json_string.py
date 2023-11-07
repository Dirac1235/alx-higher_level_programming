#!/usr/bin/python3
""" contains from json string to object converter file"""
import json


def from_json_string(my_str):
    """converts json string to python data structure"""
    json.load(my_str)
