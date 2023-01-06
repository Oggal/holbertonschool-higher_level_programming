#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
myNum = (abs(number) % 10) * (abs(number)//number)
if (myNum > 5):
    print("Last digit of {0} is {1} and is greater than 5".format(number, myNum))
elif (myNum == 0):
    print("Last digit of {0} is {1} and is 0".format(number, myNum))
else:
    print("Last digit of {0} is {1} and is less than 6 and not 0".format(number, myNum))
