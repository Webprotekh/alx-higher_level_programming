#!/usr/bin/python3
def delete_at(my_list=[], idx):
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return (my_list)
