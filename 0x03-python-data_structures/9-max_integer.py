#!/usr/bin/python3
def max_integer(my_list=[]):
    max_v = my_list[0]
    if len(my_list) == 0:
        return ("None")
    else:
        for item in my_list:
            if item > max_v:
                max_v = item
        return (max_v)
