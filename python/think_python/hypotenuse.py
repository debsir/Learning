#!/usr/bin/python

import math

def hypotenuse(leg1, leg2):
    hypotenuse = math.sqrt(leg1**2 + leg2**2)
    return hypotenuse

print hypotenuse(3, 4)
