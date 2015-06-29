#!/usr/bin/python

def most_frequent(text):
    freq = dict()
    for char in text:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1
    pool = [(value, key) for key, value in freq.items()]
    pool.sort(reverse=True)
    print pool


s = "aibhlselbhojlwecserawetbc"
most_frequent(s)



