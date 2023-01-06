#!/usr/bin/python3


def fizzbuzz():
    printtext = ""
    for i in range(1, 101):
        printtext = ""
        if (i % 3 == 0):
            printtext += "Fizz"
        if (i % 5 == 0):
            printtext += "Buzz"
        if (printtext == ""):
            printtext = "{}".format(i)
        print(printtext.format(), end=" ")
