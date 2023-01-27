#!/usr/bin/python3
'''Beam me the file scotty!'''


def write_file(filename="", text=""):
    """Open up the file, loop the lines, and print as we loop"""
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
