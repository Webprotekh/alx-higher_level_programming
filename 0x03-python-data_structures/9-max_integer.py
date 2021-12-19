#!/usr/bin/python3
def max_integer(my_list=[]):
    maxi = []
    for i in my_list:
        if i > maxi:
            maxi = i
    return maxi
