#!/usr/bin/python3

def add_integer(a:int ,b:int=98)->int:
    a = a if isinstance(a,int) else int(a) if isinstance(a, float) else None
    b = b if isinstance(b,int) else int(b) if isinstance(b, float) else None
    
    if a== None:
        raise TypeError("a must be an integer")
    if b == None:
        raise TypeError("b must be an integer")
    
    return a+b