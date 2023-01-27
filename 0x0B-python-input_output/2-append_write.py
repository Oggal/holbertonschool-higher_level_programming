#!/usr/bin/python3
'''Beam me the file scotty!'''


def append_write(filename="", text=""):
    """Open up the file, loop the lines, and print as we loop"""
    with open(filename, 'a', encoding="utf-8") as f:
        i = f.write(text)
    return i
