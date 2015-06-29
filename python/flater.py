#!/usr/bin/python

def flatter(x):
    result = []
    for lists in x:
        for i in lists:
            result.append(i)
    return result

moutain = [[4, 5, 6], [99, 100, 101], [3, 4, 5]]
print flatter(moutain)

