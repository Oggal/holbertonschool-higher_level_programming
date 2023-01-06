#!/usr/bin/python3


def uppercase(str):
    capsDiff = ord('A') - ord('a')
    l_str = list(str)
    for i, c in enumerate(str):
        if (ord(c) in range(ord('a'), ord('z')+1)):
            l_str[i] = chr(ord(c) + capsDiff)
    print("".join(l_str).format())
