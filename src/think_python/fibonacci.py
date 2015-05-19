#!/usr/bin/python

def fibonacci(n):
    if not isinstance(n, int):
        print "Fibonacci is only for integers!"
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
