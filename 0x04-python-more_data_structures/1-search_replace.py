#!/usr/bin/python3
def search_replace(my_list, search, replace):
    listReplace = my_list[:]
    for i in range(len(listReplace)):
        if listReplace[i] == search:
            listReplace[i] = replace
    return (listReplace)
