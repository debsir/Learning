#!/usr/bin/python

def long_word(word):
    return len(word) >= 20:


f = open("words.txt", "r")
while True:
    line = f.readline()
    word = line.strip()
    if long_word(word):
        print word

#Another way to traverse the file:
for line in f:
    word = line.strip()
    if long_word(word):
        print word
