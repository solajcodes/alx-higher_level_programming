#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_digit =abs(number) % 10
if number < 0:
    l_digit = l_digit * -1
if l_digit > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, l_digit))
elif l_digit == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, l_digit))
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, l_digit))




""" The output of the program should be:
The string Last digit of, followed by
the number, followed by
the string is, followed by the last digit of number, followed by
if the last digit is greater than 5: the string and is greater than 5
if the last digit is 0: the string and is 0
if the last digit is less than 6 and not 0: the string and is less than 6 and not 0
followed by a new line
"""
