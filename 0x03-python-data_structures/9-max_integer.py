#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return "None"
    else:
        max_v = my_list[0]
        for item in my_list:
            if item > max_v:
                max_v = item
        return max_v
