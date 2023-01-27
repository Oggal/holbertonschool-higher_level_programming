#!/usr/bin/python3
'''Beam me the file scotty!'''
import json


def load_from_json_file(filename):
    """From python, to Json, to disk"""
    with open(filename, 'r') as jFile:
        res = json.load(jFile)
    return res