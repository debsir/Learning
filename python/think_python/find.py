#!/usr/bin/python

def find(word, letter, start):
    if start > len(word) - 1:
        return -1
    index = start
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print find("hello", "l", 2)
