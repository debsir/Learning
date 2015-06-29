#!/usr/bin/python

def is_prime(x):
    if x == 0 or x == 1:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
        else:
            return True

for n in range(0, 101):
    if is_prime(n):
        print n,
    n += 1
