#!/usr/bin/python3


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    delims = ".?:"
    for x in set(delims):
        x_string = x+"\n\n"
        text = text.replace(x, x_string)
    text = text.replace("\n ", "\n")
    if not text.endswith("\n"):
        print(text)
    else:
        print(text, end="")
