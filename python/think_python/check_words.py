#!/usr/bin/python

def has_no_e(word):
    if "e" not in word:
        return True

def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True

def uses_only(word, required):
    for letter in word:
        if letter not in required:
            return False
    return True

def uses_all(word, required):
    for letter in required:
        if letter not in word:
            return False
    return True

def uses_all_v2(word, required):
    return uses_only(required, word)

def is_abecedarian(word):
    i = 0
    while i < len(word)-1:
        if word[i] > word[i+1]:
            return False
        i += 1
    return True

f = open("words.txt", "r")
count = 0
for line in f:
    word = line.strip()
    if is_abecedarian(word):
        print word
        count += 1

print count
