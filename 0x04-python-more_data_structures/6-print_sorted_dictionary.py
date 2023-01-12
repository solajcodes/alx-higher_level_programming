#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dic = a_dictionary
    for i in sorted(new_dic):
        print("{} : {}".format(i, new_dic[i]))
