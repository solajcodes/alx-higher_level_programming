#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_digit = abs(number) % 10
if number < 0:
    l_digit = l_digit * -1
n_str = "Last digit of {:d} is {:d}".format(number, l_digit)

if l_digit > 5:
    print("{}  and is greater than 5".format(n_str))
elif l_digit == 0:
    print("{} and is 0".format(n_str))
else:
    print("{} and is less than 6 and not 0".format(n_str))
