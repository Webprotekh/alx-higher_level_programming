#!/usr/bin/python3
def no_c(my_string):
    for i in my_string:
        if (i == chr(99) or i == chr(67)):
            continue
        print("{}".format(i), end=" ")
    print()
