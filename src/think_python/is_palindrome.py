#!/usr/bin/python

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    if len(word) == 0 or not word.isalpha():
        print "It is not a valid word!"
        return False
    elif first(word) != last(word):
        print "It is not a palindrome!"
        return False
    elif len(word) <= 3:
        print "It is a palindrome!"
        return True
    else:
        word = middle(word)
        is_palindrome(word)

def is_palindrome_v2(word):
    return word == word[::-1]

print is_palindrome_v2("lol")
