#!/usr/bin/python3
"""Add empty lines after punctuation"""


def text_indentation(text):
    '''Adds empty lines after . : or ?'''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if text=="":
        return
    delims = ".?:"
    for x in set(delims):
        x_string = x+"\n\n"
        text = text.replace(x, x_string)
    text = text.replace("\n ", "\n")
    if not text.endswith("\n"):
        print(text)
    else:
        print(text, end="")
