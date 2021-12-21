#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniqueLists = list(set(my_list))
    addLists = 0
    for i in range(len(uniqueLists)):
        addLists += uniqueLists[i]
    return (addLists)
