#!/usr/bin/python

import math
from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print bob

def triangle(t, angle, side):
    """Draw a triangle."""
    for i in range(3):
        fd(t, side)
        lt(t, 180-angle)
    
triangle(bob, angle=60, side=100)


