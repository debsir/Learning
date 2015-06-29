#!/usr/bin/python

def triple(word):
    i = 0
    count = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            i += 2
            count += 1
            if count == 3:
                return True
        else:
            i += 1
            count = 0
    return False

def triple_v2(word):
    """Regex version"""

f = open("words.txt", "r")
for line in f:
    word = line.strip()
    if triple(word):
        print word
