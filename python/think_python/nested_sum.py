#!/usr/bin/python

def nested_sum(t):
    result = 0
    for s in t:
        for i in s:
            result += i
    return result 

L = [[1, 2, 3], [4, 5], [6]]
print nested_sum(L)
