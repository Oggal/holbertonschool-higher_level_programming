#!/usr/bin/python3
'''Beam me the file scotty!'''
import json


def save_to_json(my_obj, filename):
    """From python, to Json, to disk"""
    json.dump(my_obj,filename)
   