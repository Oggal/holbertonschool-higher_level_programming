#!/usr/bin/python3
'''Beam me the file scotty!'''


def read_file(filename=""):
    """Open up the file, loop the lines, and print as we loop"""
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end="")