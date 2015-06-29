#!/usr/bin/python

def histogram(word):
    for letter in word:
        count[letter] += 1


def histogram_v2(word):
    """Create a dict adding letters for keys dynamically."""
    count = dict()
    for letter in word:
        if letter not in count:
            count[letter] = 1
        else:
            count[letter] += 1
    return count


"""Create a dict for 26 letters."""
letters = "abcdefghijklmnopqrstuvwxyz"
count = {}
for c in letters:
    count[c] = 0

f = open("words.txt", "r")
for line in f:
    word = line.strip()
    histogram(word)


