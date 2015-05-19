#!/usr/bin/python

def is_perfect(num):
    res = 0
    for i in range(1, num):
        if num % i == 0:
            res += i
    return res == num

for i in range(1, 1000000):
    if is_perfect(i):
        print i
