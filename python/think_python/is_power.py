#!/usr/bin/python

def is_power(a, b):
    if a == 1:
        return True
    elif a % b != 0:
        return False
    else:
        return is_power(a/b, b)
        
print is_power(27, 3)
