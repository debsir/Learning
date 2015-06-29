#!/usr/bin/python

def has_duplicates(L):
    sorted_L = sorted(L)
    i = 1
    while i < len(sorted_L):
        if sorted_L[i - 1] == sorted_L[i]:
            return True
        i += 1
    return False

def has_duplicates2(L):
    hist = dict()
    for i in L:
        if i in hist:
            return True
        else:
            hist[i] = 1
    return False
