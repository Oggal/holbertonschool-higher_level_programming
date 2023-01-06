#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
myNum = abs(number) % 10
if (number < 0):
    myNum *= -1
result = ""
if (myNum > 5):
    result = "greater than 5"
elif (myNum == 0):
    result = "0"
else:
    result = "less than 6 and not 0"
print("Last digit of {0} is {1} and is {2}".format(number, myNum, result))
