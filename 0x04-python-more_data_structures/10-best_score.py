#!/usr/bin/python3
def best_score(a_dictionary):
    m = 0
    scores =""
    if a_dictionary:
        for i, j in a_dictionary.items():
            if j > m:
                scores = i
                m = j
        return(scores)
    else:
        return None
