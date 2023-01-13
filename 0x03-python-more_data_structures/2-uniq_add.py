#!/usr/bin/python3


def uniq_add(my_list=[]):
    summed = []
    sum = 0
    for x in my_list:
        if x not in summed:
            summed.append(x)
            sum += x
    return sum
