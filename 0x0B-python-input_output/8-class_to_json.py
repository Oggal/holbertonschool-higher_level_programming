#!/usr/bin/python3
'''Beam me the file scotty!'''
import json


def class_to_json(obj):
    """Get dictionary representation"""
    return obj.__dict__