#!/usr/bin/python

def reverse_word(word):
    for i in range(1, len(word)+1):
        print word[-i]

def reverse_word_v2(word):
    word = word[::-1]
    for char in word:
        print char

reverse_word("hello")
reverse_word_v2("hello")
