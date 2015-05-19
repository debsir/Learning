#!/usr/bin/python

import time
"""
def file2list(rawfile):
    f = open(rawfile, "r")
    word_list = []
    for word in f:
        word_list.append(word)
    return word_list
"""

def file2list(rawfile):
    f = open(rawfile, "r")
    word_list = []
    for word in f:
        word_list = word_list + [word]
    return word_list

start = time.time()
L = file2list("words.txt")
end = time.time()
print end - start
