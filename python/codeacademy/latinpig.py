#!/usr/bin/python
word = raw_input("Please input a word in English:\n")
if not word.isalpha():
    word = raw_input("Please input a valid English word!\n")

latinpig = word[1:] + word[0] + 'ay'
print "The latinpig is %s!" % latinpig
