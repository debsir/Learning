#!/usr/bin/python

def gcd(a, b):
    if b == 0:
        return a
    else:
        """r = a % b
        a = b
        b = r
        """
        a, b = b, a % b
        return gcd(a, b)

print gcd(12345642, 5256)
