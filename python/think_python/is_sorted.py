#!/usr/bin/python

def is_sorted(L):
    i = 1
    while i < len(L):
        if L[i-1] > L[i]:
            return False
        i += 1
    return True

l = [2, 5, 7, 7, 12]
print is_sorted(l)
