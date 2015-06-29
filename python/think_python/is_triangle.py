#!/usr/bin/python

def is_triangle(a, b, c):
    sides = [a, b, c]
    sides.sort()
    if 2 * sides[2] < sum(sides):
        print "Yes, it is a triangle!"
    else:
        print "No, it isn't a triangle!"

def checker():
    numbers = raw_input("Please enter 3 numbers seperated by commas:\n")
    (a, b, c) = numbers.split(",")
    is_triangle(int(a), int(b), int(c))

while True:
    checker()
