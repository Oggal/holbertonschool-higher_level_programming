#!/usr/bin/python3
"""pascals triangle"""


def pascal_triangle(n):
    """ Create a pascal triangle"""
    tris = []
    prev = None
    for i in range(n):
        cur_layer = []
        prev_r = range(i)
        for j in range(i+1):
            if prev is None:
                cur_layer.append(1)
            else:
                a = (prev[j] if 0 <= j < len(prev) else 0)
                b = (prev[j - 1] if 0 <= j-1 < len(prev) else 0)
                cur_layer.append(a + b)
        tris.append(cur_layer)
        prev = tris[j]
    return tris

