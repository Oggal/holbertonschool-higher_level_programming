#!/usr/bin/python3


def print_last_digit(number):
    myNum = abs(number) % 10
    print("{}".format(myNum), end="")
    return (myNum)
