#!/usr/bin/python

def square_root(a):
    """Put the judgment statement in the beginning of 
    the while loop doesn't work as expected!
    """
    x = a / 2.0
    y = (x + a/x) / 2.0
    epsilon = 0.00000001
    while abs(x-y) > epsilon:
        print "Need correction!"
        y = (x + a/x) / 2.0
        x = y
#Now x is equal to y, fails the judgment statement.
    return x

print square_root(15)
