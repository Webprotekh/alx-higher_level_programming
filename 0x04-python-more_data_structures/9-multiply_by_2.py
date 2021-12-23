#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    times_2_dict = {}
    for keys in a_dictionary:
        times_2_dict[keys] = a_dictionary[keys] * 2
    return times_2_dict
