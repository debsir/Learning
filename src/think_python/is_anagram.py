#!/usr/bin/python

def is_anagram(word1, word2):
    if (word1 == word2 or 
        len(word1) != len(word2)):
        return False
    elif sorted(list(word1)) == sorted(list(word2)):
        return True
    else:
        return False
    
print is_anagram("bear", "bare")
        
