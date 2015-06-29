#!/usr/bin/python

def scatter(word):
    letters = [char for char in word]
    letters.sort()
    return tuple(letters)

def invert_dict(d):
    inverse = dict()
    for key, value in d.items():
        if value in inverse:
            inverse[value].append(key)
        else:
            inverse[value] = [key]
    return inverse

word_dict = dict()

with open("words.txt", "r") as f:
    for line in f:
        word = line.strip()
        if scatter(word) in word_dict:
            word_dict[scatter(word)].append(word)
        else:
            word_dict[scatter(word)] = [word]

anagrams_list = [(len(word_dict[fragment]), word_dict[fragment])
                 for fragment in word_dict 
                 if len(word_dict[fragment]) > 1]
"""
for fragment in word_dict:
    if len(word_dict[fragment]) > 1:
        anagrams_list.append((len(word_dict[fragment]), 
                             word_dict[fragment]))
"""

anagrams_list.sort()
for length, anagrams in anagrams_list:
    print anagrams

