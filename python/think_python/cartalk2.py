#!/usr/bin/python

def palindrome(string):
    return string == string[::-1]

for num in range(100000, 999996):
    if (palindrome(str(num)[-4:]) and 
        palindrome(str(num+1)[-5:]) and 
        palindrome(str(num+2)[-5:-1]) and 
        palindrome(str(num+3)[:])):
        print num
                
